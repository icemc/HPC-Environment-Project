@rfm.simple_test
class OSUEESSIBuildTest(rfm.RunOnlyRegressionTest):
    descr = 'Check OSU Micro-Benchmark binaries via EESSI module'
    valid_systems = ['*']
    valid_prog_environs = ['*']
    maintainers = ['Ludovic', 'Heriel', 'Franco']
    tags = {'osu', 'module', 'eessi'}

    eessi_version = variable(str, value='2023.06')  
    osu_version_in_eessi = variable(str, value='7.2')

    version = variable(str, value='7.2')
    module_name = variable(str, value='OSU-Micro-Benchmarks/7.2-gompi-2023b')
    binary_dir = variable(str, value='bin')

    @run_before('run')
    def load_modules_and_set_binary(self):
        self.prerun_cmds += [
            'module load EESSI',
            f'module load {self.module_name}'
        ]
        self.executable = 'which osu_bw'
        self.executable_opts = []

    @sanity_function
    def validate_binaries(self):
        return sn.assert_found(r'osu_bw', self.stdout)
