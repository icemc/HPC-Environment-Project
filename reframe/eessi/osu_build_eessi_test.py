import reframe as rfm
import reframe.utility.sanity as sn
import os

@rfm.simple_test
class OSUEESSIBuildTest(rfm.CompileOnlyRegressionTest):
    descr = 'Verify OSU Micro-Benchmarks availability via EESSI'
    valid_systems = ['aion:batch', 'iris:batch'] # Systems where EESSI is expected
    valid_prog_environs = ['builtin'] # We use EESSI's environment
    maintainers = ['Ludovic', 'Heriel', 'Franco']
    tags = {'osu', 'eessi', 'health'} # 'health' as it checks EESSI availability

    # EESSI Configuration
    eessi_version = variable(str, value='2023.06') # Specify your target EESSI version
    osu_version_in_eessi = variable(str, value='7.3') # OSU version expected in EESSI
    # Common toolchain for OSU in EESSI, adjust if needed
    # Example: OSU-Micro-Benchmarks/7.3-gompi-2023a
    eessi_toolchain_name = variable(str, value='gompi')
    eessi_toolchain_version = variable(str, value='2023a')


    @run_before('compile')
    def setup_eessi_environment(self):
        self.sourcesdir = None # No source code to fetch

        # Construct the expected module name based on EESSI conventions
        # This might vary slightly depending on exact EESSI naming.
        # Example: OSU-Micro-Benchmarks/7.3-gompi-2023a
        self.expected_module_name = f'OSU-Micro-Benchmarks/{self.osu_version_in_eessi}-{self.eessi_toolchain_name}-{self.eessi_toolchain_version}'

        # Commands to initialize EESSI and check for osu_bw
        # The compile_cmds are executed in the compile phase.
        # We use this phase to verify the EESSI setup.
        self.compile_cmds = [
            f'echo "Attempting to initialize EESSI version {self.eessi_version}"',
            f'source /cvmfs/eessi.io/versions/{self.eessi_version}/init/bash',
            f'echo "EESSI Initialized. Attempting to load module: {self.expected_module_name}"',
            f'module load {self.expected_module_name}',
            f'echo "Module loaded. Checking for osu_bw..."',
            'which osu_bw' # This will output the path if found
        ]
        # Since it's CompileOnly, ReFrame will execute compile_cmds.
        # The sanity function will check the output of these commands.

    @sanity_function
    def validate_eessi_osu_availability(self):
        # Check that 'which osu_bw' returned a path (i.e., not empty and not an error)
        # A more specific check might look for '/cvmfs/' in the path.
        found_osu_bw_path = sn.extractsingle(r'^(/\S+/bin/osu_bw)$', self.stdout, 1, str, default='')
        
        # Check for module load errors in stderr (though module system might print to stdout)
        module_load_error = sn.found(r'(?i)(error|fail|cannot load module)', self.stderr)
        module_not_found_eessi = sn.found(r'Unable to locate a modulefile', self.stderr) # Lmod specific

        return sn.all([
            sn.assert_not_found(r'No such file or directory.*init/bash', self.stderr,
                                msg=f"EESSI version {self.eessi_version} init script not found. Is EESSI mounted and version correct?"),
            sn.assert_true(found_osu_bw_path,
                           msg=f"osu_bw not found in PATH after attempting to load EESSI module '{self.expected_module_name}'. "
                               f"Check EESSI module name and availability. Path found: '{found_osu_bw_path}'"),
            sn.assert_false(module_load_error,
                            msg=f"Error reported during module load for '{self.expected_module_name}'."),
            sn.assert_false(module_not_found_eessi,
                            msg=f"Module '{self.expected_module_name}' not found by Lmod in EESSI."),
            sn.assert_found(rf"Successfully loaded {self.expected_module_name}", self.stderr, # Lmod often prints successful loads to stderr
                            msg=f"Lmod did not confirm successful load of '{self.expected_module_name}'. Check module output.")
        ])