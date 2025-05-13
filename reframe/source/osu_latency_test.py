import reframe as rfm
import reframe.utility.sanity as sn
import os

@rfm.simple_test
class OSULatencyTest(rfm.RunOnlyRegressionTest):
    descr = 'OSU Latency test with 8192-byte messages'
    valid_systems = ['*']
    valid_prog_environs = ['*']
    sourcesdir = None
    maintainers = ['Ludovic', 'Heriel', 'Francko']
    tags = {'osu', 'latency', 'source'} # Added 'source' tag
    num_tasks = 2
    num_cpus_per_task = 1

    # This is the directory name after the tarball is extracted
    build_prefix = 'osu-micro-benchmarks-7.2'
    message_size_bytes = 8192

    executable_opts = ['-m', f'{message_size_bytes}:{message_size_bytes}', '-x', '100', '-i', '1000']

    # Parameter for hardware topology
    variant = parameter([
        'default',
        'same_numa',
        'diff_numa_same_socket',
        'diff_socket_same_node', # Renamed for clarity
        'inter_node'
    ])

    @run_after('init')
    def set_dependencies_and_tags(self):
        self.depends_on('OSUBenchmarkBuildTest')
        self.tags.add(f'lat_{self.variant}')
        if self.variant == 'default':
            self.time_limit = '2m'
        else:
            self.time_limit = '5m'

    @run_before('run')
    def setup_variant_specifics(self):
        build_test_name = 'OSUBenchmarkBuildTest'
        build = self.getdep(build_test_name, self.current_environ.name)

        osu_binary_relative_path = os.path.join(self.build_prefix, 'c', 'mpi', 'pt2pt', 'standard', 'osu_latency')
        self.executable = os.path.join(build.stagedir, osu_binary_relative_path)

        self.job.options = []
        self.job.launcher.options = []
        self.num_tasks_per_node = 2 # Default

        if self.variant != 'inter_node':
             self.job.options += ['--exclusive']

        if self.variant == 'inter_node':
            self.num_tasks_per_node = 1
            self.job.options += ['--exclusive']
        elif self.variant == 'default':
            self.job.launcher.options += ['--cpu-bind=core']
        elif self.variant == 'same_numa':
            self.job.launcher.options += ['--cpu-bind=cores']
            if self.current_system.name == 'aion':
                self.job.options += ['--sockets-per-node=1', '--cores-per-socket=16', '--distribution=block:block']
            elif self.current_system.name == 'iris':
                self.job.options += ['--sockets-per-node=1', '--distribution=block:block']
        elif self.variant == 'diff_numa_same_socket':
            self.job.launcher.options += ['--cpu-bind=numa']
            if self.current_system.name == 'aion':
                self.job.options += ['--sockets-per-node=1', '--cores-per-socket=32', '--distribution=cyclic:cyclic', '--hint=nomultithread']
            elif self.current_system.name == 'iris':
                self.job.options += ['--sockets-per-node=1', '--distribution=cyclic:cyclic']
                self.job.launcher.options += ['--cpu-bind=numa']
        elif self.variant == 'diff_socket_same_node':
            self.job.launcher.options += ['--cpu-bind=socket']
            self.job.options += ['--ntasks-per-socket=1']

        self.descr = f'OSU Latency test ({self.message_size_bytes}B) [{self.variant}]'

    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Latency Test', self.stdout)

    @performance_function('us')
    def latency(self):
        return sn.extractsingle(rf'^\s*{self.message_size_bytes}\s+(\S+)', self.stdout, 1, float)

    @run_after('performance')
    def set_reference_values(self):
        ref_aion = {
            'default':               (3.9, -0.15, 0.15, 'us'), # Based on your prior run
            'same_numa':             (2.3, -0.15, 0.15, 'us'), # Project description typical
            'diff_numa_same_socket': (2.6, -0.15, 0.15, 'us'), # Hypothetical
            'diff_socket_same_node': (2.9, -0.15, 0.15, 'us'), # Hypothetical
            'inter_node':            (3.9, -0.10, 0.10, 'us')  # Project description typical
        }
        ref_iris = { # You MUST measure these for Iris
            'default':               (3.5, -0.15, 0.15, 'us'),
            'same_numa':             (2.0, -0.15, 0.15, 'us'),
            'diff_numa_same_socket': (2.3, -0.15, 0.15, 'us'),
            'diff_socket_same_node': (2.6, -0.15, 0.15, 'us'),
            'inter_node':            (3.5, -0.15, 0.15, 'us')
        }
        current_references = {
            'aion': ref_aion,
            'iris': ref_iris
        }
        sys_name = self.current_system.name
        if sys_name in current_references:
            self.reference = {
                f'{sys_name}:{self.current_partition.name}': {
                    'latency': current_references[sys_name][self.variant]
                }
            }
        else:
            self.reference = {'*/*': {'latency': (0, None, None, 'us')}}
