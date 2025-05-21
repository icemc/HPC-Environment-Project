import reframe as rfm
import reframe.utility.sanity as sn
import os

@rfm.simple_test
class OSUBandwidthTest(rfm.RunOnlyRegressionTest):
    descr = 'OSU Bandwidth test with 1MB messages (Source Build)'
    valid_systems = ['aion:batch', 'iris:batch']
    valid_prog_environs = ['foss-2023b']
    sourcesdir = None
    maintainers = ['Ludovic', 'Heriel', 'Franco']
    tags = {'osu', 'bandwidth', 'source'}
    num_tasks = 2
    num_cpus_per_task = 1

    build_prefix = 'osu-micro-benchmarks-7.2'
    message_size_bytes = 1048576
    executable_opts = ['-m', f'{message_size_bytes}:{message_size_bytes}', '-x', '10', '-i', '100']

    variant = parameter([
        'default',
        'same_numa',
        'diff_numa_same_socket',
        'diff_socket_same_node',
        'inter_node'
    ])

    @run_after('init')
    def set_dependencies_and_tags(self):
        self.depends_on('OSUBenchmarkBuildTest')
        self.tags.add(f'bw_{self.variant}')
        if self.variant == 'default' or self.variant == 'inter_node':
            self.time_limit = '3m'
        else:
            self.time_limit = '5m'

    @run_before('run')
    def setup_variant_specifics(self):
        build_test_name = 'OSUBenchmarkBuildTest'
        build = self.getdep(build_test_name)

        osu_binary_relative_path = os.path.join(f'osu-micro-benchmarks-{build.version}', 'c', 'mpi', 'pt2pt', 'standard', 'osu_bw')
        self.executable = os.path.join(build.stagedir, osu_binary_relative_path)

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
                # Iris Regular Skylake: 14 cores/socket, 1 socket = 1 NUMA
                self.job.options.extend(['--sockets-per-node=1', '--cores-per-socket=14', '--distribution=block:block', '--hint=nomultithread'])
        elif self.variant == 'diff_numa_same_socket':
            if self.current_system.name == 'aion':
                # Aion: Request 1 socket, 32 cores (2 NUMA regions)
                self.job.options.extend(['--sockets-per-node=1', '--cores-per-socket=32', '--hint=nomultithread'])
            elif self.current_system.name == 'iris':
                # Iris: 1 socket = 1 NUMA (14 cores). This variant will behave like 'same_numa'.
                # Allocate 1 socket (1 NUMA node). OMPI will map both tasks to this single NUMA node.
                self.job.options.extend(['--sockets-per-node=1', '--cores-per-socket=14', '--distribution=block:block', '--hint=nomultithread'])

            self.env_vars = {
                'OMPI_MCA_rmaps_base_mapping_policy': 'numa:PE=1',
                'OMPI_MCA_hwloc_base_binding_policy': 'numa',
            }
        elif self.variant == 'diff_socket_same_node':
            self.job.launcher.options.append('--cpu-bind=socket')
            self.job.options.append('--ntasks-per-socket=1')
            if self.current_system.name == 'iris': # Ensure we get enough cores for 2 tasks on 2 sockets
                self.job.options.append(f'--cores-per-socket=1') # Request at least 1 core per allocated socket for the task

        self.descr = f'OSU Bandwidth test (1MB, Src) [{self.variant}]'

    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Bandwidth Test', self.stdout)

    @performance_function('MB/s')
    def bandwidth(self):
        return sn.extractsingle(rf'^\s*{self.message_size_bytes}\s+(\S+)', self.stdout, 1, float)

    @run_after('performance')
    def set_reference_values(self):
        ref_aion = { # Based on your Aion runs
            'default':               (11900, -0.10, 0.10, 'MB/s'),
            'same_numa':             (14400, -0.10, 0.10, 'MB/s'),
            'diff_numa_same_socket': (13500, -0.20, 0.20, 'MB/s'), # Assuming it works
            'diff_socket_same_node': (10800, -0.10, 0.10, 'MB/s'),
            'inter_node':            (12300, -0.10, 0.10, 'MB/s')
        }
        ref_iris = { # Based on your Iris runs, same_numa failed, diff_numa_same_socket needs re-eval
            'default':               (16800, -0.10, 0.10, 'MB/s'),
            'same_numa':             (17000, -0.20, 0.20, 'MB/s'), # Placeholder, needs measurement
            'diff_numa_same_socket': (18300, -0.10, 0.10, 'MB/s'), # Will likely be like same_numa
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
