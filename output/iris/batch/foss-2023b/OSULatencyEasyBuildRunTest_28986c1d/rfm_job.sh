#!/bin/bash
#SBATCH --job-name="rfm_OSULatencyEasyBuildRunTest_28986c1d"
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
module load tools/EasyBuild
export OMPI_MCA_rmaps_base_mapping_policy=numa:PE=1
export OMPI_MCA_hwloc_base_binding_policy=numa
echo "--- START PRERUN CMDS for Latency diff_numa_same_socket ---"
echo "DEBUG: osu_build_fixture.stagedir = /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUEasyBuildCompileTest"
echo "DEBUG: Path for 'module use': /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/modules/all"
echo "DEBUG: Listing contents of path for 'module use':"
ls -lR /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/modules/all || echo "Path not found or empty: /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/modules/all"
module use /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/modules/all
echo "DEBUG: MODULEPATH after 'module use': $MODULEPATH"
echo "DEBUG: Available OSU modules after 'module use':"
module avail OSU-Micro-Benchmarks || echo "OSU-Micro-Benchmarks module still not available after use cmd"
echo "DEBUG: Explicitly trying to load module: OSU-Micro-Benchmarks/7.2-foss-2023b"
module load OSU-Micro-Benchmarks/7.2-foss-2023b || echo "ERROR: module load OSU-Micro-Benchmarks/7.2-foss-2023b FAILED IN PRERUN"
echo "DEBUG: Modules loaded after explicit load (LMOD_CMD list):"
$LMOD_CMD list || echo "LMOD_CMD list failed"
echo "DEBUG: Original PATH: $PATH"
export PATH="/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/software/OSU-Micro-Benchmarks/7.2-foss-2023b/libexec/osu-micro-benchmarks/mpi/pt2pt:$PATH"
echo "DEBUG: Modified PATH: $PATH"
echo "DEBUG: Verifying executable osu_latency in new PATH: $(which osu_latency || echo osu_latency not in PATH)"
echo "--- END PRERUN CMDS ---"
srun --cpus-per-task=1 osu_latency -m 8192:8192 -x 100 -i 1000
