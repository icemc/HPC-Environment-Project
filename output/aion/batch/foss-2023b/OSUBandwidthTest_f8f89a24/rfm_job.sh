#!/bin/bash
#SBATCH --job-name="rfm_OSUBandwidthTest_f8f89a24"
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_job.out
#SBATCH --error=rfm_job.err
#SBATCH --time=0:3:0
#SBATCH --partition=batch
#SBATCH --qos=normal
#SBATCH --time=0-00:10:00
#SBATCH --exclusive
module load env/testing/2023b
module load toolchain/foss/2023b
module load tools/EasyBuild
srun --cpus-per-task=1 --cpu-bind=core /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUBenchmarkBuildTest/osu-micro-benchmarks-7.2/c/mpi/pt2pt/standard/osu_bw -m 1048576:1048576 -x 10 -i 100
