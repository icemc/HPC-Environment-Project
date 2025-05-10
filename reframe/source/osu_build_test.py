import reframe as rfm
import reframe.utility.sanity as sn
from pathlib import Path

@rfm.simple_test
class OSUBenchmarkBuildTest(rfm.RegressionTest):
    descr = 'Compile OSU Micro-Benchmark 7.2 from source'
    valid_systems = ['*']
    valid_prog_environs = ['*']
    sourcesdir = None
    source_url = 'https://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-7.2.tar.gz'
    build_system = 'Make'
    maintainers = ['you']
    tags = {'osu', 'build'}

    @run_before('compile')
    def prepare_build(self):
        self.prebuild_cmds = [
            f'wget {self.source_url}',
            'tar -xzf osu-micro-benchmarks-7.2.tar.gz',
            'mkdir -p install'
        ]
        self.build_system.make_opts = ['-C osu-micro-benchmarks-7.2/mpi']
        self.build_system.builddir = 'osu-micro-benchmarks-7.2/mpi'
        self.build_system.max_concurrency = 1

    @run_after('compile')
    def copy_binaries(self):
        self.postbuild_cmds = [
            'cp osu-micro-benchmarks-7.2/mpi/osu_* install/'
        ]

    @sanity_function
    def validate_binaries(self):
        return sn.all([
            sn.assert_found('osu_latency', 'install/osu_latency'),
            sn.assert_found('osu_bw', 'install/osu_bw')
        ])

    @run_after('setup')
    def set_install_path(self):
        self.install_path = Path(self.stagedir) / 'install'
