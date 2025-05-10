import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class OSULatencyTest(rfm.RunOnlyRegressionTest):
    descr = 'OSU Latency test with 8192-byte messages'
    valid_systems = ['*']
    valid_prog_environs = ['*']
    sourcesdir = None
    maintainers = ['you']
    tags = {'osu', 'latency'}
    num_tasks = 2
    num_tasks_per_node = 2
    message_size = 8192
    executable_opts = ['-m', '8192', '8192']

    # Parameter for hardware topology
    variant = parameter([
        'default',               # scheduler decides
        'same_numa',             # pin to same NUMA node
        'diff_numa_same_socket', # different NUMA, same socket
        'diff_socket',           # different sockets, same node
        'inter_node'             # 2 different nodes
    ])

    @run_after('init')
    def set_dependencies(self):
        self.depends_on('OSUBenchmarkBuildTest', how='require')

    @run_before('run')
    def setup_variant(self):
        build = self.depends_on('OSUBenchmarkBuildTest')
        self.executable = f'{build.stagedir}/install/osu_latency'

        self.job.options = []
        self.time_limit = '5m'

        if self.variant == 'inter_node':
            self.num_tasks_per_node = 1
            self.num_tasks = 2
        else:
            self.num_tasks_per_node = 2
            self.num_tasks = 2

        # Bindings: actual control depends on MPI + scheduler
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
        return sn.assert_found(r'# OSU MPI Latency Test', self.stdout)

    @performance_function('us')
    def latency(self):
        return sn.extractsingle(r'^\s*8192\s+(\S+)', self.stdout, 1, float)

    @run_after('performance')
    def set_reference(self):
        references = {
            'default': (2.3, None, 0.1, 'us'),
            'same_numa': (2.3, None, 0.1, 'us'),
            'diff_numa_same_socket': (2.8, None, 0.2, 'us'),
            'diff_socket': (3.1, None, 0.2, 'us'),
            'inter_node': (3.9, None, 0.2, 'us')
        }
        self.reference = {'*': {'latency': references[self.variant]}}
