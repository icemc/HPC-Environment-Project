import reframe as rfm
import reframe.utility.sanity as sn
import os

_THIS_FILE_DIR = os.path.dirname(os.path.realpath(__file__))

@rfm.simple_test
class OSUEasyBuildCompileTest(rfm.CompileOnlyRegressionTest):
    descr = 'Build OSU MB 7.2 via EB (using foss/2023b from local .eb)'
    valid_systems = ['aion:batch', 'iris:batch']
    valid_prog_environs = ['foss-2023b'] 
    
    # Assumes OSU-Micro-Benchmarks-7.2-foss-2023b.eb is in the same dir as this script
    easyconfig_to_use = 'OSU-Micro-Benchmarks-7.2-foss-2023b.eb' 
    
    build_system = 'EasyBuild'
    
    def __init__(self):
        super().__init__()
        # Tell EasyBuild to use already loaded modules if they match, otherwise warn.
        self.build_system.options = getattr(self.build_system, 'options', []) + ['--detect-loaded-modules=warn']
    
    expected_module_name = variable(str, value='OSU-Micro-Benchmarks/7.2-foss-2023b')

    @run_before('compile')
    def stage_easyconfig_file_and_set_eb_options(self):
        source_eb_file_path = os.path.join(_THIS_FILE_DIR, self.easyconfig_to_use)
        staged_eb_filename = self.easyconfig_to_use 
        
        self.prebuild_cmds = [
            f'echo "DEBUG [Build]: _THIS_FILE_DIR (test definition dir) = {_THIS_FILE_DIR}"',
            f'echo "DEBUG [Build]: Source .eb file path = {source_eb_file_path}"',
            f'echo "DEBUG [Build]: Copying {source_eb_file_path} to {os.path.join(self.stagedir, staged_eb_filename)}"',
            f'cp "{source_eb_file_path}" "{os.path.join(self.stagedir, staged_eb_filename)}"',
            f'echo "DEBUG [Build]: Verifying staged .eb file: $(ls -l {os.path.join(self.stagedir, staged_eb_filename)} || echo STAGED_EB_NOT_FOUND)"',
            'echo "DEBUG [Build]: Initial loaded modules: $($LMOD_CMD list || echo LMOD_CMD_failed)"'
        ]
        
        self.build_system.easyconfigs = [staged_eb_filename]
        self.build_system.robot_paths = []

    @sanity_function
    def validate_easybuild_build(self):
        sn.assert_not_found(r'ERROR: Can\'t find path', self.stderr,
                             msg="EasyBuild itself reported it could not find the .eb file path.")
        return sn.assert_found(r'(?i)(\bBuild Succeeded\b|Build succeeded for|easyblock_step INFO build succeeded)', self.stdout,
                                   msg="EasyBuild did not report successful compilation or an error occurred.")
