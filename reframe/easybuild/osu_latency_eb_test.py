import reframe as rfm
import reframe.utility.sanity as sn
import os

@rfm.simple_test
class OSULatencyEasyBuildRunTest(rfm.RunOnlyRegressionTest):
    descr = 'OSU Latency test (8192B) using EasyBuild compiled binary'
    valid_systems = ['aion:batch', 'iris:batch']
    valid_prog_environs = ['foss-2023b']
    
    sourcesdir = None
    maintainers = ['Ludovic', 'Heriel', 'Francko']
    tags = {'osu', 'latency', 'easybuild'}

    num_tasks = 2
    num_cpus_per_task = 1
    message_size_bytes = 8192
    executable_opts = ['-m', f'{message_size_bytes}:{message_size_bytes}', '-x', '100', '-i', '1000']
    
    variant = parameter([
        'default', 'same_numa', 'diff_numa_same_socket',
        'diff_socket_same_node', 'inter_node'
    ])
    
    built_osu_module_name = variable(str, value='OSU-Micro-Benchmarks/7.2-foss-2023b')
    # This will be set in setup_run_environment_and_placement
    # self.executable is just the command name, PATH will be set.

    @run_after('init')
    def set_dependencies_and_tags(self):
        self.depends_on('OSUEasyBuildCompileTest')
        self.tags.add(f'lat_eb_{self.variant}')
        if self.variant == 'default' or self.variant == 'inter_node':
            self.time_limit = '3m'
        else:
            self.time_limit = '5m'

    @run_before('run')
    def setup_run_environment_and_placement(self):
        osu_build_fixture = self.getdep('OSUEasyBuildCompileTest')

        # Path to the 'modules/all' directory created by EasyBuild
        relative_module_tree_base = "easybuild/modules/all" 
        absolute_module_tree_for_module_use = os.path.join(osu_build_fixture.stagedir, relative_module_tree_base)
        
        # Path to the actual executables
        relative_exec_path_base = os.path.join("easybuild", "software", "OSU-Micro-Benchmarks", "7.2-foss-2023b", "libexec", "osu-micro-benchmarks", "mpi", "pt2pt")
        absolute_exec_path = os.path.join(osu_build_fixture.stagedir, relative_exec_path_base)
        
        self.modules_path = [] 
        
        self.prerun_cmds = [
            f'echo "--- START PRERUN CMDS for Latency {self.variant} ---"',
            f'echo "DEBUG: osu_build_fixture.stagedir = {osu_build_fixture.stagedir}"',
            f'echo "DEBUG: Path for \'module use\': {absolute_module_tree_for_module_use}"',
            f'echo "DEBUG: Listing contents of path for \'module use\':"',
            f'ls -lR {absolute_module_tree_for_module_use} || echo "Path not found or empty: {absolute_module_tree_for_module_use}"',
            f'module use {absolute_module_tree_for_module_use}', 
            f'echo "DEBUG: MODULEPATH after \'module use\': $MODULEPATH"',
            f'echo "DEBUG: Available OSU modules after \'module use\':"',
            'module avail OSU-Micro-Benchmarks || echo "OSU-Micro-Benchmarks module still not available after use cmd"',
            f'echo "DEBUG: Explicitly trying to load module: {self.built_osu_module_name}"',
            f'module load {self.built_osu_module_name} || echo "ERROR: module load {self.built_osu_module_name} FAILED IN PRERUN"',
            'echo "DEBUG: Modules loaded after explicit load (LMOD_CMD list):"',
            '$LMOD_CMD list || echo "LMOD_CMD list failed"',
            f'echo "DEBUG: Original PATH: $PATH"',
            f'export PATH="{absolute_exec_path}:$PATH"',
            f'echo "DEBUG: Modified PATH: $PATH"',
            f'echo "DEBUG: Verifying executable osu_latency in new PATH: $(which osu_latency || echo osu_latency not in PATH)"',
            'echo "--- END PRERUN CMDS ---"'
        ]
        
        self.modules = [] # ReFrame will not generate 'module load' for these
        self.executable = 'osu_latency' # Should be found via modified PATH
        
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
                 
        self.descr = f'OSU Latency test ({self.message_size_bytes}B, EB) [{self.variant}]'

    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Latency Test', self.stdout)

    @performance_function('us')
    def latency(self):
        return sn.extractsingle(rf'^\s*{self.message_size_bytes}\s+(\S+)', self.stdout, 1, float)

    @run_after('performance')
    def set_reference_values(self):
        ref_aion = {
            'default':               (2.3, -0.20, 0.20, 'us'),
            'same_numa':             (0.6, -0.30, 0.30, 'us'),
            'diff_numa_same_socket': (2.0, -0.30, 0.30, 'us'),
            'diff_socket_same_node': (2.3, -0.20, 0.20, 'us'),
            'inter_node':            (4.5, -0.15, 0.15, 'us')
        }
        ref_iris = { 
            'default':               (4.5, -0.15, 0.15, 'us'),
            'same_numa':             (1.0, -0.30, 0.30, 'us'), 
            'diff_numa_same_socket': (4.4, -0.15, 0.15, 'us'), 
            'diff_socket_same_node': (3.0, -0.25, 0.25, 'us'), 
            'inter_node':            (4.6, -0.15, 0.15, 'us')
        }
        current_references = {'aion': ref_aion, 'iris': ref_iris}
        sys_name = self.current_system.name
        partition_name = self.current_partition.name
        if sys_name in current_references:
            self.reference = {f'{sys_name}:{partition_name}': {'latency': current_references[sys_name][self.variant]}}
        else:
            self.reference = {'*/*': {'latency': (0, None, None, 'us')}}
