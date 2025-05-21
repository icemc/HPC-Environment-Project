import reframe as rfm
import reframe.utility.sanity as sn
import os

@rfm.simple_test
class OSULatencyTest(rfm.RunOnlyRegressionTest):
    descr = 'OSU Latency test with 8192-byte messages (EESSI)'
    valid_systems = ['*']
    valid_prog_environs = ['foss-2023b']
    sourcesdir = None
    maintainers = ['Ludovic', 'Heriel', 'Franco']
    tags = {'osu', 'latency', 'eessi'}
    num_tasks = 2
    num_cpus_per_task = 1

    message_size_bytes = 8192
    executable_opts = ['-m', f'{message_size_bytes}:{message_size_bytes}', '-x', '100', '-i', '1000']

    variant = parameter([
        'default',
        'same_numa',
        'diff_numa_same_socket',
        'diff_socket_same_node',
        'inter_node'
    ])

    @run_after('init')
    def set_dependencies_and_tags(self):
        self.depends_on('OSUEESSIBuildTest')
        self.tags.add(f'lat_{self.variant}')
        if self.variant == 'default' or self.variant == 'inter_node':
            self.time_limit = '3m'
        else:
            self.time_limit = '5m'


    @run_before('run')
    def load_eessi_modules(self):
        # Ensure the environment from the dependency is reused
        self.prerun_cmds += [
            'module load EESSI',
            'module load OSU-Micro-Benchmarks/7.2-gompi-2023b'
        ]

    @run_before('run')
    def setup_variant_specifics(self):
        self.executable = 'osu_latency'

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
            self.env_vars.update({
                'OMPI_MCA_rmaps_base_mapping_policy': 'numa:PE=1',
                'OMPI_MCA_hwloc_base_binding_policy': 'numa',
            })
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
