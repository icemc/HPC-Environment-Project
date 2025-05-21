import reframe as rfm
import reframe.utility.sanity as sn
import os

@rfm.simple_test
class OSUBandwidthEasyBuildRunTest(rfm.RunOnlyRegressionTest):
    descr = 'OSU Bandwidth test (1MB) using EasyBuild compiled binary'
    valid_systems = ['aion:batch', 'iris:batch']
    valid_prog_environs = ['foss-2023b']
    
    sourcesdir = None
    maintainers = ['Ludovic', 'Heriel', 'Francko']
    tags = {'osu', 'bandwidth', 'easybuild'}

    num_tasks = 2
    num_cpus_per_task = 1
    message_size_bytes = 1048576
    executable_opts = ['-m', f'{message_size_bytes}:{message_size_bytes}', '-x', '10', '-i', '100']

    variant = parameter([
        'default', 'same_numa', 'diff_numa_same_socket',
        'diff_socket_same_node', 'inter_node'
    ])

    built_osu_module_name = variable(str, value='OSU-Micro-Benchmarks/7.2-foss-2023b')

    @run_after('init')
    def set_dependencies_and_tags(self):
        self.depends_on('OSUEasyBuildCompileTest')
        self.tags.add(f'bw_eb_{self.variant}')
        if self.variant == 'default' or self.variant == 'inter_node':
            self.time_limit = '3m'
        else:
            self.time_limit = '5m'

    @run_before('run')
    def setup_run_environment_and_placement(self):
        osu_build_fixture = self.getdep('OSUEasyBuildCompileTest')

        relative_module_tree_base = "easybuild/modules/all" 
        absolute_module_tree_for_use_cmd = os.path.join(osu_build_fixture.stagedir, relative_module_tree_base)
        
        self.modules_path = []
        
        self.prerun_cmds = [
            f'echo "DEBUG [Run Test - {self.variant}]: osu_build_fixture.stagedir = {osu_build_fixture.stagedir}"',
            f'echo "DEBUG [Run Test - {self.variant}]: Absolute path for \'module use\': {absolute_module_tree_for_use_cmd}"',
            f'echo "DEBUG [Run Test - {self.variant}]: Listing contents of path for \'module use\':"',
            f'ls -lR {absolute_module_tree_for_use_cmd} || echo "Path not found or empty: {absolute_module_tree_for_use_cmd}"',
            f'module use {absolute_module_tree_for_use_cmd}',
            f'echo "DEBUG [Run Test - {self.variant}]: MODULEPATH after \'module use\': $MODULEPATH"',
            f'echo "DEBUG [Run Test - {self.variant}]: Available OSU modules after \'module use\':"',
            'module avail OSU-Micro-Benchmarks || echo "OSU-Micro-Benchmarks module still not available"',
            f'echo "DEBUG [Run Test - {self.variant}]: Trying to load module by name: {self.built_osu_module_name}"'
        ]
        
        self.modules = [self.built_osu_module_name]

        if "OSULatency" in type(self).__name__: 
            self.executable = 'osu_latency'
            self.descr_prefix = f'OSU Latency test ({self.message_size_bytes}B, EB)'
        elif "OSUBandwidth" in type(self).__name__:
            self.executable = 'osu_bw'
            self.descr_prefix = f'OSU Bandwidth test ({self.message_size_bytes // (1024*1024)}MB, EB)'
        else:
            self.executable = 'osu_bw' 
            self.descr_prefix = 'OSU Bandwidth Test (EB)'

        self.job.options = []
        self.job.launcher.options = []
        self.env_vars = {}
        self.num_tasks_per_node = 2

        if self.variant not in ['inter_node']:
            self.job.options.append('--exclusive')

        if self.variant == 'inter_node':
            self.num_tasks_per_node = 1
            self.job.options.append('--exclusive')
        elif self.variant == 'default':
            self.job.launcher.options.append('--cpu-bind=core')
        elif self.variant == 'same_numa':
            self.job.launcher.options.append('--cpu-bind=cores')
            if self.current_system.name == 'aion':
                self.job.options.extend(['--sockets-per-node=1', '--cores-per-socket=16', '--distribution=block:block', '--hint=nomultithread'])
            elif self.current_system.name == 'iris':
                self.job.options.extend(['--sockets-per-node=1', '--cores-per-socket=14', '--distribution=block:block', '--hint=nomultithread'])
        elif self.variant == 'diff_numa_same_socket':
            if self.current_system.name == 'aion':
                self.job.options.extend(['--sockets-per-node=1', '--cores-per-socket=32', '--hint=nomultithread'])
            elif self.current_system.name == 'iris':
                self.job.options.extend(['--sockets-per-node=1', '--cores-per-socket=14', '--distribution=block:block', '--hint=nomultithread'])
            self.env_vars = {
                'OMPI_MCA_rmaps_base_mapping_policy': 'numa:PE=1',
                'OMPI_MCA_hwloc_base_binding_policy': 'numa',
            }
        elif self.variant == 'diff_socket_same_node':
            self.job.launcher.options.append('--cpu-bind=socket')
            self.job.options.append('--ntasks-per-socket=1')
            if self.current_system.name == 'iris':
                 self.job.options.append(f'--cores-per-socket=1')
                 
        self.descr = f'{self.descr_prefix} [{self.variant}]'

    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Bandwidth Test', self.stdout)

    @performance_function('MB/s')
    def bandwidth(self):
        return sn.extractsingle(rf'^\s*{self.message_size_bytes}\s+(\S+)', self.stdout, 1, float)

    @run_after('performance')
    def set_reference_values(self):
        ref_aion = {
            'default':               (11800, -0.10, 0.10, 'MB/s'),
            'same_numa':             (14200, -0.10, 0.10, 'MB/s'),
            'diff_numa_same_socket': (13500, -0.25, 0.25, 'MB/s'),
            'diff_socket_same_node': (10800, -0.10, 0.10, 'MB/s'),
            'inter_node':            (12300, -0.10, 0.10, 'MB/s')
        }
        ref_iris = { 
            'default':               (16800, -0.10, 0.10, 'MB/s'),
            'same_numa':             (17000, -0.20, 0.20, 'MB/s'), 
            'diff_numa_same_socket': (18300, -0.10, 0.10, 'MB/s'), 
            'diff_socket_same_node': (17600, -0.10, 0.10, 'MB/s'),
            'inter_node':            (10000, -0.10, 0.10, 'MB/s')
        }
        current_references = {'aion': ref_aion, 'iris': ref_iris}
        sys_name = self.current_system.name
        partition_name = self.current_partition.name
        if sys_name in current_references:
            self.reference = {f'{sys_name}:{partition_name}': {'bandwidth': current_references[sys_name][self.variant]}}
        else:
            self.reference = {'*/*': {'bandwidth': (0, None, None, 'MB/s')}}
