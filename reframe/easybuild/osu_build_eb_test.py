import reframe as rfm
import reframe.utility.sanity as sn
import os

@rfm.simple_test
class OSUEasyBuildCompileTest(rfm.CompileOnlyRegressionTest):
    descr = 'Compile OSU MB 7.2 via EB (using foss/2023b from modified .eb)'
    valid_systems = ['aion:batch', 'iris:batch']
    valid_prog_environs = ['foss-2023b']
    
    easyconfig_filename = 'OSU-Micro-Benchmarks-7.2-gompi-2023.09.eb' 
    
    build_system = 'EasyBuild'
    
    def __init__(self):
        super().__init__()
        self.build_system.options = getattr(self.build_system, 'options', []) + ['--detect-loaded-modules=warn']
    
    expected_module_name = variable(str, value='OSU-Micro-Benchmarks/7.2-foss-2023b')

    @run_before('compile')
    def stage_easyconfig_file(self):
        source_eb_relative_path = os.path.join('easyconfigs', 'o', 'OSU-Micro-Benchmarks', self.easyconfig_filename)
        source_eb_absolute_path = os.path.abspath(os.path.join(self.prefix, source_eb_relative_path))
        staged_eb_filename = self.easyconfig_filename 
        
        self.prebuild_cmds = [
            f'echo "DEBUG [Build]: self.prefix (test dir) = {self.prefix}"',
            f'echo "DEBUG [Build]: Source .eb file absolute path = {source_eb_absolute_path}"',
            f'echo "DEBUG [Build]: Staging .eb file to: {os.path.join(self.stagedir, staged_eb_filename)}"',
            f'cp "{source_eb_absolute_path}" "{os.path.join(self.stagedir, staged_eb_filename)}"',
            f'echo "DEBUG [Build]: Verifying staged .eb file: $(ls -l {os.path.join(self.stagedir, staged_eb_filename)} || echo STAGED_EB_NOT_FOUND)"',
            'echo "DEBUG [Build]: Initial MODULEPATH before EB execution: $MODULEPATH"',
            'echo "DEBUG [Build]: Which eb before EB execution: $(which eb || echo eb not in PATH)"',
            'echo "DEBUG [Build]: Initial loaded modules before EB execution (from LMOD_CMD): $($LMOD_CMD list || echo LMOD_CMD_failed)"'
        ]
        self.build_system.easyconfigs = [staged_eb_filename]
        self.build_system.robot_paths = [] 

    @sanity_function
    def validate_easybuild_compilation(self):
        sn.assert_not_found(r'ERROR: Can\'t find path', self.stderr,
                             msg="EasyBuild itself reported it could not find the .eb file path.")
        return sn.assert_found(r'(?i)(\bBuild Succeeded\b|Build succeeded for|easyblock_step INFO build succeeded)', self.stdout,
                                   msg="EasyBuild did not report successful compilation or an error occurred.")
