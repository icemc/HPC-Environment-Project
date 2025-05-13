sadsdasdasdasdasd0 [fkusek@aion-0002 HPC-Environment-Project](7931575 1N/T/1CN)$ reframe -C reframe/configs/configs.py -c reframe/source -r --performance-report
[ReFrame Setup]
  version:           4.7.4
  command:           '/opt/apps/easybuild/systems/aion/rhel810-20250405/2023b/epyc/software/ReFrame/4.7.4-GCCcore-13.2.0/bin/reframe -C reframe/configs/configs.py -c reframe/source -r --performance-report'
  launched by:       fkusek@aion-0002
  working directory: '/mnt/aiongpfs/users/fkusek/HPC-Environment-Project'
  settings files:    '<builtin>', 'reframe/configs/configs.py'
  selected system:   'aion'
  check search path: '/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/reframe/source'
  stage directory:   '/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage'
  output directory:  '/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/output'
  log files:         '/tmp/rfm-ylqhjw1d.log'
  results database:  '/home/users/fkusek/.reframe/reports/results.db'

[==========] Running 11 check(s)
[==========] Started on Tue May 13 01:59:20 2025+0200

[----------] start processing checks
[ RUN      ] OSUBenchmarkBuildTest /d61c3c51 @aion:batch+foss-2023b
[       OK ] ( 1/11) OSUBenchmarkBuildTest /d61c3c51 @aion:batch+foss-2023b
[ RUN      ] OSULatencyTest %variant=inter_node /e5e4cb74 @aion:batch+foss-2023b
[ RUN      ] OSULatencyTest %variant=diff_socket_same_node /cab6c957 @aion:batch+foss-2023b
[ RUN      ] OSULatencyTest %variant=diff_numa_same_socket /362b6d20 @aion:batch+foss-2023b
[ RUN      ] OSULatencyTest %variant=same_numa /f802e61c @aion:batch+foss-2023b
[ RUN      ] OSULatencyTest %variant=default /b51639f0 @aion:batch+foss-2023b
[ RUN      ] OSUBandwidthTest %variant=inter_node /5716a367 @aion:batch+foss-2023b
[ RUN      ] OSUBandwidthTest %variant=diff_socket_same_node /e306891b @aion:batch+foss-2023b
[ RUN      ] OSUBandwidthTest %variant=diff_numa_same_socket /7b6f5ad4 @aion:batch+foss-2023b
[ RUN      ] OSUBandwidthTest %variant=same_numa /fb083019 @aion:batch+foss-2023b
[ RUN      ] OSUBandwidthTest %variant=default /f8f89a24 @aion:batch+foss-2023b
[       OK ] ( 2/11) OSULatencyTest %variant=inter_node /e5e4cb74 @aion:batch+foss-2023b
P: latency: 4.0 us (r:0, l:None, u:None)
[       OK ] ( 3/11) OSULatencyTest %variant=diff_socket_same_node /cab6c957 @aion:batch+foss-2023b
P: latency: 2.29 us (r:0, l:None, u:None)
[     FAIL ] ( 4/11) OSULatencyTest %variant=diff_numa_same_socket /362b6d20 @aion:batch+foss-2023b
==> test failed during 'sanity': test staged in '/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSULatencyTest_362b6d20'
[       OK ] ( 5/11) OSULatencyTest %variant=same_numa /f802e61c @aion:batch+foss-2023b
P: latency: 0.59 us (r:0, l:None, u:None)
[       OK ] ( 6/11) OSULatencyTest %variant=default /b51639f0 @aion:batch+foss-2023b
P: latency: 2.28 us (r:0, l:None, u:None)
[       OK ] ( 7/11) OSUBandwidthTest %variant=inter_node /5716a367 @aion:batch+foss-2023b
P: bandwidth: 12328.11 MB/s (r:0, l:None, u:None)
[       OK ] ( 8/11) OSUBandwidthTest %variant=diff_socket_same_node /e306891b @aion:batch+foss-2023b
P: bandwidth: 10855.48 MB/s (r:0, l:None, u:None)
[     FAIL ] ( 9/11) OSUBandwidthTest %variant=diff_numa_same_socket /7b6f5ad4 @aion:batch+foss-2023b
==> test failed during 'sanity': test staged in '/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUBandwidthTest_7b6f5ad4'
[       OK ] (10/11) OSUBandwidthTest %variant=same_numa /fb083019 @aion:batch+foss-2023b
P: bandwidth: 14294.99 MB/s (r:0, l:None, u:None)
[       OK ] (11/11) OSUBandwidthTest %variant=default /f8f89a24 @aion:batch+foss-2023b
P: bandwidth: 10924.04 MB/s (r:0, l:None, u:None)
[----------] all spawned checks have finished

[  FAILED  ] Ran 11/11 test case(s) from 11 check(s) (2 failure(s), 0 skipped, 0 aborted)
[==========] Finished on Tue May 13 02:07:32 2025+0200
============================= SUMMARY OF FAILURES ==============================
--------------------------------------------------------------------------------
FAILURE INFO for OSULatencyTest %variant=diff_numa_same_socket (run: 1/1)
  * Description: OSU Latency test (8192B) [diff_numa_same_socket]
  * System partition: aion
  * Environment: foss-2023b
  * Test file: /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/reframe/source/osu_latency_test.py
  * Stage directory: /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSULatencyTest_362b6d20
  * Node list: aion-0229
  * Job type: batch job (id=7931637)
  * Dependencies (conceptual): ['OSUBenchmarkBuildTest']
  * Dependencies (actual): [('OSUBenchmarkBuildTest', 'aion:batch', 'foss-2023b')]
  * Maintainers: ['Ludovic', 'Heriel', 'Francko']
  * Failing phase: sanity
  * Rerun with '-n /362b6d20 -p foss-2023b --system aion -r'
  * Reason: sanity error: pattern '# OSU MPI Latency Test' not found in 'rfm_job.out'
--- rfm_job.out (last 10 lines) ---
--- rfm_job.out ------ rfm_job.err (last 10 lines) ---
srun: error: unrecognized --cpu-bind argument "numa"
srun: fatal: Failed to parse --cpu-bind= values.
--- rfm_job.err ---
--------------------------------------------------------------------------------
FAILURE INFO for OSUBandwidthTest %variant=diff_numa_same_socket (run: 1/1)
  * Description: OSU Bandwidth test (1MB) [diff_numa_same_socket]
  * System partition: aion
  * Environment: foss-2023b
  * Test file: /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/reframe/source/osu_bw_test.py
  * Stage directory: /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUBandwidthTest_7b6f5ad4
  * Node list: aion-0232
  * Job type: batch job (id=7931647)
  * Dependencies (conceptual): ['OSUBenchmarkBuildTest']
  * Dependencies (actual): [('OSUBenchmarkBuildTest', 'aion:batch', 'foss-2023b')]
  * Maintainers: ['Ludovic', 'Heriel', 'Francko']
  * Failing phase: sanity
  * Rerun with '-n /7b6f5ad4 -p foss-2023b --system aion -r'
  * Reason: sanity error: pattern '# OSU MPI Bandwidth Test' not found in 'rfm_job.out'
--- rfm_job.out (last 10 lines) ---
--- rfm_job.out ------ rfm_job.err (last 10 lines) ---
srun: error: unrecognized --cpu-bind argument "numa"
srun: fatal: Failed to parse --cpu-bind= values.
--- rfm_job.err ---
--------------------------------------------------------------------------------

============================== PERFORMANCE REPORT ==============================

┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━┯━━━━━━━━━┯━━━━━━━━━┯━━━━━━━━━━┑
│ name                                            │ sysenv                │ job_nodelist        │ pvar      │ punit   │    pval │ result   │
┝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━┿━━━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━━┥
│ OSULatencyTest %variant=inter_node              │ aion:batch+foss-2023b │ aion-0229,aion-0231 │ latency   │ us      │       4 │ pass     │
├─────────────────────────────────────────────────┼───────────────────────┼─────────────────────┼───────────┼─────────┼─────────┼──────────┤
│ OSULatencyTest %variant=diff_socket_same_node   │ aion:batch+foss-2023b │ aion-0232           │ latency   │ us      │    2.29 │ pass     │
├─────────────────────────────────────────────────┼───────────────────────┼─────────────────────┼───────────┼─────────┼─────────┼──────────┤
│ OSULatencyTest %variant=same_numa               │ aion:batch+foss-2023b │ aion-0231           │ latency   │ us      │    0.59 │ pass     │
├─────────────────────────────────────────────────┼───────────────────────┼─────────────────────┼───────────┼─────────┼─────────┼──────────┤
│ OSULatencyTest %variant=default                 │ aion:batch+foss-2023b │ aion-0232           │ latency   │ us      │    2.28 │ pass     │
├─────────────────────────────────────────────────┼───────────────────────┼─────────────────────┼───────────┼─────────┼─────────┼──────────┤
│ OSUBandwidthTest %variant=inter_node            │ aion:batch+foss-2023b │ aion-0229,aion-0231 │ bandwidth │ MB/s    │ 12328.1 │ pass     │
├─────────────────────────────────────────────────┼───────────────────────┼─────────────────────┼───────────┼─────────┼─────────┼──────────┤
│ OSUBandwidthTest %variant=diff_socket_same_node │ aion:batch+foss-2023b │ aion-0232           │ bandwidth │ MB/s    │ 10855.5 │ pass     │
├─────────────────────────────────────────────────┼───────────────────────┼─────────────────────┼───────────┼─────────┼─────────┼──────────┤
│ OSUBandwidthTest %variant=same_numa             │ aion:batch+foss-2023b │ aion-0229           │ bandwidth │ MB/s    │   14295 │ pass     │
├─────────────────────────────────────────────────┼───────────────────────┼─────────────────────┼───────────┼─────────┼─────────┼──────────┤
│ OSUBandwidthTest %variant=default               │ aion:batch+foss-2023b │ aion-0231           │ bandwidth │ MB/s    │   10924 │ pass     │
┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━┷━━━━━━━━━━━┷━━━━━━━━━┷━━━━━━━━━┷━━━━━━━━━━┙

