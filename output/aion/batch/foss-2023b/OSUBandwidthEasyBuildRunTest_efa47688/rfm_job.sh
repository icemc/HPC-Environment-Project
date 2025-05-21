#!/bin/bash
#SBATCH --job-name="rfm_OSUBandwidthEasyBuildRunTest_efa47688"
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=1
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
echo "--- START PRERUN CMDS for Bandwidth inter_node ---"
echo "DEBUG: osu_build_fixture.stagedir = /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest"
echo "DEBUG: Path for 'module use': /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/modules/all"
echo "DEBUG: Listing contents of path for 'module use':"
ls -lR /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/modules/all || echo "Path not found or empty: /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/modules/all"
module use /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/modules/all
echo "DEBUG: MODULEPATH after 'module use': $MODULEPATH"
echo "DEBUG: Available OSU modules after 'module use':"
module avail OSU-Micro-Benchmarks || echo "OSU-Micro-Benchmarks module still not available after use cmd"
echo "DEBUG: Explicitly trying to load module: OSU-Micro-Benchmarks/7.2-foss-2023b"
module load OSU-Micro-Benchmarks/7.2-foss-2023b || echo "ERROR: module load OSU-Micro-Benchmarks/7.2-foss-2023b FAILED IN PRERUN"
echo "DEBUG: Modules loaded after explicit load (LMOD_CMD list):"
$LMOD_CMD list || echo "LMOD_CMD list failed"
echo "DEBUG: Original PATH: $PATH"
export PATH="/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/software/OSU-Micro-Benchmarks/7.2-foss-2023b/libexec/osu-micro-benchmarks/mpi/pt2pt:$PATH"
echo "DEBUG: Modified PATH: $PATH"
echo "DEBUG: Verifying executable osu_bw in new PATH: $(which osu_bw || echo osu_bw not in PATH)"
echo "--- END PRERUN CMDS ---"
srun --cpus-per-task=1 osu_bw -m 1048576:1048576 -x 10 -i 100
