import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class OSUEESSIBuildTest(rfm.RunOnlyRegressionTest):
    descr = 'Check OSU Micro-Benchmark binaries via EESSI module'
    valid_systems = ['aion:batch', 'iris:batch']
    valid_prog_environs = ['foss-2023b']
    maintainers = ['Ludovic', 'Heriel', 'Francko']
    tags = {'osu', 'module', 'eessi'}

    module_name = variable(str, value='OSU-Micro-Benchmarks/7.2-gompi-2023b')

    @run_before('run')
    def load_modules_and_set_binary(self):
        self.prerun_cmds += [
            'module load EESSI',
            f'module load {self.module_name}'
        ]
        self.executable = 'which'
        self.executable_opts = ['osu_bw']  # Check if osu_bw is in $PATH

    @sanity_function
    def validate_binary_found(self):
        return sn.assert_found(r'osu_bw', self.stdout)
