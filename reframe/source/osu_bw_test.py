import reframe as rfm
import reframe.utility.sanity as sn
import os

@rfm.simple_test
class OSUBandwidthTest(rfm.RunOnlyRegressionTest):
    descr = 'OSU Bandwidth test with 1MB messages'
    valid_systems = ['*'] # Will be filtered by ReFrame config
    valid_prog_environs = ['*'] # Will be filtered by ReFrame config
    sourcesdir = None
    maintainers = ['Ludovic', 'Heriel', 'Francko']
    tags = {'osu', 'bandwidth', 'source'} # Added 'source' tag
    num_tasks = 2
    num_cpus_per_task = 1 # Default, ensure 1 MPI rank per core

    # This is the directory name after the tarball is extracted,
    # as used in your OSUBenchmarkBuildTest
    build_prefix = 'osu-micro-benchmarks-7.2'
    message_size_bytes = 1048576

    executable_opts = ['-m', f'{message_size_bytes}:{message_size_bytes}', '-x', '10', '-i', '100']

    # Parameter for hardware topology
    variant = parameter([
        'default', # Both tasks on one node, default Slurm/MPI binding
        'same_numa',
        'diff_numa_same_socket',
        'diff_socket_same_node', # Renamed for clarity
        'inter_node'
    ])

    @run_after('init')
    def set_dependencies_and_tags(self):
        self.depends_on('OSUBenchmarkBuildTest')
        # Add a tag for the variant to make it easier to select specific tests
        self.tags.add(f'bw_{self.variant}')
        if self.variant == 'default':
            self.time_limit = '2m' # Default might be quick
        else:
            self.time_limit = '5m' # Other variants might take slightly longer with specific pinning

    @run_before('run')
    def setup_variant_specifics(self):
        build_test_name = 'OSUBenchmarkBuildTest'
        # Get the dependency, ensuring it's from the same environment
        build = self.getdep(build_test_name, self.current_environ.name)

        osu_binary_relative_path = os.path.join(self.build_prefix, 'c', 'mpi', 'pt2pt', 'standard', 'osu_bw')
        self.executable = os.path.join(build.stagedir, osu_binary_relative_path)

        self.job.options = []  # For sbatch options
        self.job.launcher.options = [] # For srun options (the launcher)

        # Default to 2 tasks on one node
        self.num_tasks_per_node = 2

        # Add --exclusive for most tests for stable results
        if self.variant != 'inter_node': # inter_node handles nodes separately
             self.job.options += ['--exclusive']

        if self.variant == 'inter_node':
            self.num_tasks_per_node = 1
            # self.num_tasks is already 2
            # No specific srun binding needed by default, but can add --cpu-bind=core if desired
            # self.job.launcher.options += ['--cpu-bind=core']
            self.job.options += ['--exclusive'] # Request exclusive access to each of the 2 nodes
        elif self.variant == 'default':
            # Default placement on a single node, usually packed by Slurm.
            # Explicitly bind to cores for consistency.
            self.job.launcher.options += ['--cpu-bind=core']
        elif self.variant == 'same_numa':
            self.job.launcher.options += ['--cpu-bind=cores'] # srun: bind tasks to cores
            if self.current_system.name == 'aion':
                # Aion: AMD Rome, 8 NUMA nodes of 16 cores each (4 NUMA/socket)
                # Constrain job to one socket, and only enough cores for one NUMA region
                self.job.options += [
                    '--sockets-per-node=1',
                    '--cores-per-socket=16', # Request cores of one NUMA region
                    '--distribution=block:block' # Pack tasks into these cores
                ]
            elif self.current_system.name == 'iris':
                # Iris: Intel. Assume 1 NUMA node per socket for this example. Adjust if different.
                # This effectively pins to a single socket/NUMA.
                self.job.options += ['--sockets-per-node=1', '--distribution=block:block']
        elif self.variant == 'diff_numa_same_socket':
            self.job.launcher.options += ['--cpu-bind=numa'] # srun: bind tasks to NUMA nodes
            if self.current_system.name == 'aion':
                # Try to get tasks on different NUMA nodes of the *same* socket.
                # Request one socket, but enough cores to span at least two NUMA nodes (e.g., 2*16=32)
                # Slurm's cyclic distribution over NUMA nodes within the allocation might work.
                self.job.options += [
                    '--sockets-per-node=1',
                    '--cores-per-socket=32', # Request cores spanning two NUMA regions
                    '--distribution=cyclic:cyclic', # Spread tasks within the allocation
                    '--hint=nomultithread' # Avoid SMT if it confuses NUMA placement
                ]
            elif self.current_system.name == 'iris':
                # If Iris has 2 NUMA nodes per socket (e.g., sub-NUMA clustering on some Intel Xeons)
                # A similar strategy might apply. If 1 NUMA per socket, this case is same as 'diff_socket_same_node'.
                # For simplicity, let's assume this might behave like 'diff_socket_same_node' or needs specific hwloc pinning.
                # Fallback to a general binding attempt for Iris:
                self.job.options += ['--sockets-per-node=1', '--distribution=cyclic:cyclic']
                self.job.launcher.options += ['--cpu-bind=numa'] # srun: bind tasks to NUMA nodes

        elif self.variant == 'diff_socket_same_node':
            self.job.launcher.options += ['--cpu-bind=socket'] # srun: bind tasks to sockets
            # sbatch option to ensure Slurm allocates one task to each socket:
            self.job.options += ['--ntasks-per-socket=1']

        self.descr = f'OSU Bandwidth test (1MB) [{self.variant}]' # Update description

    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Bandwidth Test', self.stdout)

    @performance_function('MB/s')
    def bandwidth(self):
        # Regex to find the line with the message size and extract the bandwidth value
        return sn.extractsingle(rf'^\s*{self.message_size_bytes}\s+(\S+)', self.stdout, 1, float)

    @run_after('performance')
    def set_reference_values(self):
        # These are initial placeholders, adjust after collecting data
        # Format: (value, lower_threshold_rel_or_abs, upper_threshold_rel_or_abs, unit)
        # Using relative thresholds (e.g., -0.1 for -10%, 0.2 for +20%)
        # Using None for lower/upper means no check for that bound.
        # (target_value, None, 0.1, 'unit') means target_value with +10% tolerance, no lower bound.
        # (target_value, -0.05, 0.05, 'unit') means target_value +/- 5%.

        ref_aion = {
            'default':               (14000, -0.15, 0.15, 'MB/s'),
            'same_numa':             (14500, -0.15, 0.15, 'MB/s'),
            'diff_numa_same_socket': (13500, -0.15, 0.15, 'MB/s'),
            'diff_socket_same_node': (13000, -0.15, 0.15, 'MB/s'),
            'inter_node':            (12000, -0.10, 0.10, 'MB/s') # From project description
        }
        ref_iris = { # You MUST measure these for Iris
            'default':               (13000, -0.15, 0.15, 'MB/s'),
            'same_numa':             (13500, -0.15, 0.15, 'MB/s'),
            'diff_numa_same_socket': (12500, -0.15, 0.15, 'MB/s'),
            'diff_socket_same_node': (12000, -0.15, 0.15, 'MB/s'),
            'inter_node':            (11000, -0.15, 0.15, 'MB/s')
        }

        current_references = {
            'aion': ref_aion,
            'iris': ref_iris
        }
        
        # Apply to the current system (e.g., 'aion:batch' or 'iris:batch')
        # self.reference requires a dict mapping system:partition to perf refs
        sys_name = self.current_system.name
        if sys_name in current_references:
            self.reference = {
                f'{sys_name}:{self.current_partition.name}': {
                    'bandwidth': current_references[sys_name][self.variant]
                }
            }
        else:
            # Fallback if system name from ReFrame config isn't 'aion' or 'iris'
            self.reference = {'*/*': {'bandwidth': (0, None, None, 'MB/s')}}
