#!/bin/bash

_onerror()
{
    exitcode=$?
    echo "-reframe: command \`$BASH_COMMAND' failed (exit code: $exitcode)"
    exit $exitcode
}

trap _onerror ERR

module load env/testing/2023b
module load toolchain/foss/2023b
module load tools/EasyBuild
echo "DEBUG [Build]: self.prefix (test dir) = /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/reframe/easybuild"
echo "DEBUG [Build]: Source .eb file absolute path = /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/reframe/easybuild/easyconfigs/o/OSU-Micro-Benchmarks/OSU-Micro-Benchmarks-7.2-gompi-2023.09.eb"
echo "DEBUG [Build]: Staging .eb file to: /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/OSU-Micro-Benchmarks-7.2-gompi-2023.09.eb"
cp "/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/reframe/easybuild/easyconfigs/o/OSU-Micro-Benchmarks/OSU-Micro-Benchmarks-7.2-gompi-2023.09.eb" "/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/OSU-Micro-Benchmarks-7.2-gompi-2023.09.eb"
echo "DEBUG [Build]: Verifying staged .eb file: $(ls -l /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/OSU-Micro-Benchmarks-7.2-gompi-2023.09.eb || echo STAGED_EB_NOT_FOUND)"
echo "DEBUG [Build]: Initial MODULEPATH before EB execution: $MODULEPATH"
echo "DEBUG [Build]: Which eb before EB execution: $(which eb || echo eb not in PATH)"
echo "DEBUG [Build]: Initial loaded modules before EB execution (from LMOD_CMD): $($LMOD_CMD list || echo LMOD_CMD_failed)"
export EASYBUILD_BUILDPATH=/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/build
export EASYBUILD_INSTALLPATH=/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild
export EASYBUILD_PREFIX=/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild
export EASYBUILD_SOURCEPATH=/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild
eb OSU-Micro-Benchmarks-7.2-gompi-2023.09.eb --detect-loaded-modules=warn
