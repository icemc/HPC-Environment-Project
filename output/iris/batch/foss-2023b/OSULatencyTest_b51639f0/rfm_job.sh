#!/bin/bash
#SBATCH --job-name="rfm_OSULatencyTest_b51639f0"
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_job.out
#SBATCH --error=rfm_job.err
#SBATCH --time=0:3:0
#SBATCH --partition=batch
#SBATCH --qos=normal
#SBATCH -C skylake
#SBATCH --time=0-00:10:00
#SBATCH --exclusive
module load env/testing/2023b
module load toolchain/foss/2023b
srun --cpus-per-task=1 --cpu-bind=core /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUBenchmarkBuildTest/osu-micro-benchmarks-7.2/c/mpi/pt2pt/standard/osu_latency -m 8192:8192 -x 100 -i 1000
