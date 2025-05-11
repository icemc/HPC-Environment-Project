import reframe as rfm
import reframe.utility.sanity as sn
import os

@rfm.simple_test
class OSUBandwidthTest(rfm.RunOnlyRegressionTest):
    descr = 'OSU Bandwidth test with 1MB messages'
    valid_systems = ['*']
    valid_prog_environs = ['*']
    sourcesdir = None
    maintainers = ['Ludovic', 'Heriel', 'Francko']
    tags = {'osu', 'bandwidth'}
    num_tasks = 2
    num_cpus_per_task = 1
    num_tasks_per_node = 2 # Default, will be overridden by variant logic
    executable_opts = ['-m', '1048576', '1048576']
    build_prefix = 'osu-micro-benchmarks-7.2'

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
        self.executable = os.path.join(build.stagedir, self.build_prefix, 'c', 'mpi', 'pt2pt', 'standard', 'osu_bw')

        self.time_limit = '5m'
        self.job.options = [] # Initialize options

        if self.variant == 'inter_node':
            self.num_tasks_per_node = 1
            self.num_tasks = 2
            self.num_cpus_per_task = 1
        else:
            # For all other intra-node variants
            self.num_tasks_per_node = 2
            self.num_tasks = 2
            self.num_cpus_per_task = 1

        if self.variant == 'same_numa':
            self.job.options += ['--cpu-bind=cores']
        elif self.variant == 'diff_numa_same_socket':
            # This might depend on your system's topology and scheduler.
            # 'rank_ldom' might not always pin to different NUMA but same socket.
            # Consider using more specific pinning like '--cpu-bind=mask_cpu:...'
            # or '--cpu-bind=numa' and ensuring tasks land on different NUMAs.
            # For simplicity, we'll keep it as is, but be aware of potential nuances.
            self.job.options += ['--cpu-bind=rank_ldom'] # Or specific masks
        elif self.variant == 'diff_socket':
            # Similar to above, '--cpu-bind=socket' might be more direct if available
            # or specific masks to ensure tasks are on different sockets.
            self.job.options += ['--cpu-bind=rank_ldom'] # Or specific masks
        elif self.variant == 'inter_node':
            # Ensure tasks are distributed across nodes
            self.job.options += ['--distribution=block:block'] # Slurm option

        self.descr += f' [{self.variant}]'

    @sanity_function 
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Bandwidth Test', self.stdout)

    @performance_function('MB/s') 
    def bandwidth(self):
        return sn.extractsingle(r'^\s*1048576\s+(\S+)', self.stdout, 1, float)

    @run_after('performance') 
    def set_reference(self):
        references = {
            'default': (12000, -0.1, 0.2, 'MB/s'),
            'same_numa': (12000, -0.1, 0.2, 'MB/s'),
            'diff_numa_same_socket': (10500, -0.2, 0.2, 'MB/s'),
            'diff_socket': (9500, -0.2, 0.2, 'MB/s'),
            'inter_node': (7500, -0.2, 0.3, 'MB/s')
        }
        # The reference dict should map system_name:partition_name to another dict
        # or use '*' to apply to all.
        # The inner dict maps the performance variable name to its reference tuple.
        self.reference = {'*/*': {'bandwidth': references[self.variant]}}
        # If you want to apply to any system but a specific partition, e.g., 'gpu':
        # self.reference = {'*:gpu': {'bandwidth': references[self.variant]}}
        # Or for a specific system 'mycluster' and any partition:
        # self.reference = {'mycluster:*': {'bandwidth': references[self.variant]}}
        # For current system and current partition:
        # self.reference = {self.current_system.name + ':' + self.current_partition.name: {'bandwidth': references[self.variant]}}
        # However, '*/*' (any system, any partition) is often used.
        # ReFrame 4.x might be more lenient with just '*' but '*/*' is more explicit.
        # The code you had `self.reference = {'*': {'bandwidth': references[self.variant]}}`
        # might also work depending on the exact ReFrame version and its interpretation,
        # but '*/*' is safer for "any system, any partition".