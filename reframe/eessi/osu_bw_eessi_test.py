import reframe as rfm
import reframe.utility.sanity as sn
import os

@rfm.simple_test
class OSUEESSIBandwidthTest(rfm.RunOnlyRegressionTest):
    descr = 'OSU Bandwidth test with 1MB messages (EESSI)'
    valid_systems = ['aion:batch', 'iris:batch'] # Systems where EESSI is expected
    # Using 'builtin' as we rely on EESSI for MPI and toolchain
    valid_prog_environs = ['builtin']
    sourcesdir = None
    maintainers = ['Ludovic', 'Heriel', 'Franco']
    tags = {'osu', 'bandwidth', 'eessi'}
    num_tasks = 2
    num_cpus_per_task = 1

    message_size_bytes = 1048576
    executable_opts = ['-m', f'{message_size_bytes}:{message_size_bytes}', '-x', '10', '-i', '100']

    variant = parameter([
        'default',
        'same_numa',
        'diff_numa_same_socket',
        'diff_socket_same_node',
        'inter_node'
    ])

    @run_after('init')
    def set_dependencies_and_tags(self):
        self.depends_on('OSUEESSIBuildTest')
        self.tags.add(f'bw_{self.variant}')
        if self.variant == 'default' or self.variant == 'inter_node':
            self.time_limit = '3m'
        else:
            self.time_limit = '5m'

    @run_before('run')
    def setup_variant_specifics(self):
        build_test_name = 'OSUEESSIBuildTest'
        build_dep = self.getdep(build_test_name) # Get the dependency object

        # Commands to run before the main executable (srun/mpirun)
        # This is crucial for EESSI: initialize EESSI in the job script.
        self.prerun_cmds = [
            f'source /cvmfs/eessi.io/versions/{build_dep.eessi_version}/init/bash'
        ]

        # Load the EESSI OSU module identified by the build_dep test
        self.modules = [build_dep.expected_module_name]
        self.executable = 'osu_bw' # Should be in PATH after module load

        self.job.options = []
        self.job.launcher.options = []
        self.env_vars = {} # EESSI's module should set up MPI environment
        self.num_tasks_per_node = 2

        if self.variant not in ['inter_node']:
            self.job.options.append('--exclusive')

        if self.variant == 'inter_node':
            self.num_tasks_per_node = 1
            self.job.options.append('--exclusive')
        elif self.variant == 'default':
            # EESSI's MPI should handle binding, or we can provide hints
            # Depending on the MPI in EESSI (OpenMPI, Intel MPI), options might differ
            # For OpenMPI (common in EESSI gompi)
            self.job.launcher.options.append('--cpu-bind=core')
        elif self.variant == 'same_numa':
            self.job.launcher.options.append('--cpu-bind=cores') # OpenMPI
            if self.current_system.name == 'aion':
                self.job.options.extend(['--sockets-per-node=1', '--cores-per-socket=16', '--distribution=block:block', '--hint=nomultithread'])
            elif self.current_system.name == 'iris':
                self.job.options.extend(['--sockets-per-node=1', '--cores-per-socket=14', '--distribution=block:block', '--hint=nomultithread'])
        elif self.variant == 'diff_numa_same_socket':
            # This depends heavily on the MPI implementation and system architecture
            # Assuming OpenMPI from EESSI's gompi
            if self.current_system.name == 'aion':
                self.job.options.extend(['--sockets-per-node=1', '--cores-per-socket=32', '--hint=nomultithread'])
            elif self.current_system.name == 'iris':
                self.job.options.extend(['--sockets-per-node=1', '--cores-per-socket=14', '--distribution=block:block', '--hint=nomultithread'])
            # OpenMPI specific environment variables for mapping
            self.env_vars.update({
                'OMPI_MCA_rmaps_base_mapping_policy': 'numa:PE=1',
                'OMPI_MCA_hwloc_base_binding_policy': 'numa',
            })
        elif self.variant == 'diff_socket_same_node':
            self.job.launcher.options.append('--cpu-bind=socket') # OpenMPI
            self.job.options.append('--ntasks-per-socket=1')
            if self.current_system.name == 'iris':
                self.job.options.append(f'--cores-per-socket=1')

        self.descr = f'OSU Bandwidth test (1MB, EESSI {build_dep.eessi_version}, OSU {build_dep.osu_version_in_eessi}) [{self.variant}]'

    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Bandwidth Test', self.stdout)

    @performance_function('MB/s')
    def bandwidth(self):
        return sn.extractsingle(rf'^\s*{self.message_size_bytes}\s+(\S+)', self.stdout, 1, float)

    @run_after('performance')
    def set_reference_values(self):
        # NOTE: These reference values are copied.
        # Performance with EESSI's OSU might differ. Adjust as needed.
        ref_aion = {
            'default':               (11900, -0.10, 0.10, 'MB/s'),
            'same_numa':             (14400, -0.10, 0.10, 'MB/s'),
            'diff_numa_same_socket': (13500, -0.20, 0.20, 'MB/s'),
            'diff_socket_same_node': (10800, -0.10, 0.10, 'MB/s'),
            'inter_node':            (12300, -0.10, 0.10, 'MB/s')
        }
        ref_iris = {
            'default':               (16800, -0.10, 0.10, 'MB/s'),
            'same_numa':             (17000, -0.20, 0.20, 'MB/s'),
            'diff_numa_same_socket': (18300, -0.10, 0.10, 'MB/s'),
            'diff_socket_same_node': (17600, -0.10, 0.10, 'MB/s'),
            'inter_node':            (10000, -0.10, 0.10, 'MB/s')
        }
        current_references = {'aion': ref_aion, 'iris': ref_iris}
        sys_name = self.current_system.name
        partition_name = self.current_partition.name

        self.reference = {'*/*': {'bandwidth': (0, None, None, 'MB/s')}}
        if sys_name in current_references and self.variant in current_references[sys_name]:
            ref_key = f'{sys_name}:{partition_name}'
            self.reference[ref_key] = {'bandwidth': current_references[sys_name][self.variant]}