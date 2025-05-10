import os
import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class OSUBenchmarkBuildTest(rfm.CompileOnlyRegressionTest):
    descr = 'Compile OSU Micro-Benchmark 7.2 from source'
    valid_systems = ['*']
    valid_prog_environs = ['*']
    maintainers = ['Ludovic', 'Heriel', 'Francko']
    tags = {'osu', 'build'}
    version = '7.2'
    source_tarball = f'osu-micro-benchmarks-{version}.tar.gz'
    source_url = f'https://mvapich.cse.ohio-state.edu/download/mvapich/{source_tarball}'
    source_subdir = f'osu-micro-benchmarks-{version}/c/mpi'

    @run_before('compile')
    def prepare_build(self):
        self.prebuild_cmds = [
            f'wget {self.source_url}',
            f'tar -xzf {self.source_tarball}',
            f'cd {self.source_subdir} && ./configure CC=mpicc'
        ]
        self.build_system = 'Make'
        self.build_system.makefile = None  # Use default Makefile
        self.build_system.max_concurrency = 1
        self.build_system.options = []
        self.build_system.srcdir = self.source_subdir

    @sanity_function
    def validate_build(self):
        return sn.assert_exists(os.path.join(self.stagedir, self.source_subdir, 'osu_latency'))
