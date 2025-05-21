import os
import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class OSUBenchmarkBuildTest(rfm.CompileOnlyRegressionTest):
    descr = 'Compile OSU Micro-Benchmark 7.2 from source'
    valid_systems = ['*']
    valid_prog_environs = ['*']
    maintainers = ['Ludovic', 'Heriel', 'Franco']
    tags = {'osu', 'build'}

    build_prefix = variable(str)
    version = variable(str, value='7.2')

    source_tarball = f'osu-micro-benchmarks-{version}.tar.gz'
    source_url = f'https://mvapich.cse.ohio-state.edu/download/mvapich/{source_tarball}'

    @run_before('compile')
    def prepare_build(self):
        self.build_prefix = self.source_tarball[:-7]
        self.prebuild_cmds = [
            f'wget {self.source_url}',
            f'tar -xzf {self.source_tarball}',
            f'cd {self.build_prefix}'
        ]
        self.build_system = 'Autotools'
        self.build_system.max_concurrency =  8
        self.build_system.options = []

    @sanity_function
    def validate_build(self):
        path = os.path.join(self.stagedir, self.build_prefix, 'c', 'mpi', 'pt2pt', 'standard', 'osu_bw')
        return sn.assert_true(os.path.exists(path))
