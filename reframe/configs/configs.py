
# ReFrame configuration for ULHPC cluster (both Iris and Aion)

site_configuration = {
  'systems': [
    {
      'name': 'iris',
      'descr': 'Iris cluster',
      'hostnames': [r'iris-[0-9]{3}'],
      'modules_system': 'lmod',
      'partitions': [
        {
          'name': 'batch',
          'descr': 'Iris compute nodes',
          'scheduler': 'slurm',
          'launcher': 'srun',
          'access': ['--partition=batch', '--qos=normal', '-C skylake', '--time=0-00:10:00'],
          'environs': ['foss-2023b'],
          'max_jobs': 8,
        },
      ]
    },
    {
      'name': 'aion',
      'descr': 'Aion compute nodes',
      'hostnames': [r'aion-[0-9]{4}'],
      'modules_system': 'lmod',
      'partitions': [
        {
          'name': 'batch',
          'descr': 'Aion compute nodes',
          'scheduler': 'slurm',
          'launcher': 'srun',
          'access': ['--partition=batch', '--qos=normal', '--time=0-00:10:00'],
          'environs': ['foss-2023b'],
          'max_jobs': 8,
        }
      ]
    }
  ],

  'environments': [
    {
      'name': 'foss-2023b',
      'modules': [
        'env/testing/2023b', 
        'toolchain/foss/2023b' 
      ],
      
      # compilers for this environment
      'cc': 'mpicc',
      'cxx': 'mpicxx',
      'ftn': 'mpifort',
    },
    # We can add other environments later (e.g., EESSI)
    # reframe --config-file configs/configs.py -c source/osu_build_test.py -c source/osu_bw_test.py -c source/osu_latency_test.py  -r
  ],
}