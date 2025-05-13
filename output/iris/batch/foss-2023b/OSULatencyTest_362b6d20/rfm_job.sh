#!/bin/bash
#SBATCH --job-name="rfm_OSULatencyTest_362b6d20"
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_job.out
#SBATCH --error=rfm_job.err
#SBATCH --time=0:5:0
#SBATCH --partition=batch
#SBATCH --qos=normal
#SBATCH -C skylake
#SBATCH --time=0-00:10:00
#SBATCH --exclusive
#SBATCH --sockets-per-node=1
#SBATCH --cores-per-socket=14
#SBATCH --distribution=block:block
#SBATCH --hint=nomultithread
module load env/testing/2023b
module load toolchain/foss/2023b
export OMPI_MCA_rmaps_base_mapping_policy=numa:PE=1
export OMPI_MCA_hwloc_base_binding_policy=numa
srun --cpus-per-task=1 /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUBenchmarkBuildTest/osu-micro-benchmarks-7.2/c/mpi/pt2pt/standard/osu_latency -m 8192:8192 -x 100 -i 1000
