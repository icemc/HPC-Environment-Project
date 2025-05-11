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
    tags = {'osu', 'latency'}
    num_tasks = 2
    num_cpus_per_task = 1
    num_tasks_per_node = 2 # Default, overridden by variant logic
    message_size = 8192 
    executable_opts = ['-m', str(message_size), str(message_size)] 
    build_prefix = 'osu-micro-benchmarks-7.2'

    # Parameter for hardware topology
    variant = parameter([
        'default',
        'same_numa',
        'diff_numa_same_socket',
        'diff_socket',
        'inter_node'
    ])

    @run_after('init') 
    def set_dependencies(self):
        self.depends_on('OSUBenchmarkBuildTest')

    @run_before('run') 
    def setup_variant(self):
        build = self.getdep('OSUBenchmarkBuildTest')
        self.executable = os.path.join(build.stagedir, self.build_prefix, 'c', 'mpi', 'pt2pt', 'standard', 'osu_latency')

        self.job.options = [] # Initialize options
        self.time_limit = '5m'

        if self.variant == 'inter_node':
            self.num_tasks_per_node = 1
            self.num_tasks = 2
            self.num_cpus_per_task = 1
        else:
            # For all other intra-node variants
            self.num_tasks_per_node = 2
            self.num_tasks = 2
            self.num_cpus_per_task = 1

        # Bindings: actual control depends on MPI + scheduler
        if self.variant == 'same_numa':
            self.job.options += ['--cpu-bind=cores']
        elif self.variant == 'diff_numa_same_socket':
            # Note: '--cpu-bind=rank_ldom' behavior can be complex.
            # Verify this achieves the intended pinning on your specific system.
            self.job.options += ['--cpu-bind=rank_ldom']
        elif self.variant == 'diff_socket':
            # Similar to above, verify the pinning.
            self.job.options += ['--cpu-bind=rank_ldom']
        elif self.variant == 'inter_node':
            self.job.options += ['--distribution=block:block'] # Slurm option

        self.descr += f' [{self.variant}]'

    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Latency Test', self.stdout)

    @performance_function('us')
    def latency(self):
        # Ensure the regex correctly matches the message size used in executable_opts
        return sn.extractsingle(rf'^\s*{self.message_size}\s+(\S+)', self.stdout, 1, float)

    @run_after('performance') 
    def set_reference(self):
        references = {
            'default': (2.3, None, 0.1, 'us'),
            'same_numa': (2.3, None, 0.1, 'us'),
            'diff_numa_same_socket': (2.8, None, 0.2, 'us'),
            'diff_socket': (3.1, None, 0.2, 'us'),
            'inter_node': (3.9, None, 0.2, 'us')
        }
        # Use '*/*' for "any system, any partition" for robustness
        self.reference = {'*/*': {'latency': references[self.variant]}}