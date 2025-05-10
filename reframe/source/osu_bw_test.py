import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class OSUBandwidthTest(rfm.RunOnlyRegressionTest):
    descr = 'OSU Bandwidth test with 1MB messages'
    valid_systems = ['*']
    valid_prog_environs = ['*']
    sourcesdir = None
    maintainers = ['Ludovic', 'Heriel', 'Francko']
    tags = {'osu', 'bandwidth'}
    num_tasks = 2
    num_tasks_per_node = 2
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
        build = self.use_dependency('OSUBenchmarkBuildTest')
        self.executable = os.path.join(build.stagedir, self.build_prefix, 'c', 'mpi', 'pt2pt', 'standard', 'osu_bw')

        self.time_limit = '5m'
        self.job.options = []

        if self.variant == 'inter_node':
            self.num_tasks_per_node = 1
            self.num_tasks = 2
        else:
            self.num_tasks_per_node = 2
            self.num_tasks = 2

        if self.variant == 'same_numa':
            self.job.options += ['--cpu-bind=cores']
        elif self.variant == 'diff_numa_same_socket':
            self.job.options += ['--cpu-bind=rank_ldom']
        elif self.variant == 'diff_socket':
            self.job.options += ['--cpu-bind=rank_ldom']
        elif self.variant == 'inter_node':
            self.job.options += ['--distribution=block:block']

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
        self.reference = {'*': {'bandwidth': references[self.variant]}}
