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
echo "DEBUG [Build]: _THIS_FILE_DIR (test definition dir) = /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/reframe/easybuild"
echo "DEBUG [Build]: Source .eb file path = /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/reframe/easybuild/OSU-Micro-Benchmarks-7.2-foss-2023b.eb"
echo "DEBUG [Build]: Copying /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/reframe/easybuild/OSU-Micro-Benchmarks-7.2-foss-2023b.eb to /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUEasyBuildCompileTest/OSU-Micro-Benchmarks-7.2-foss-2023b.eb"
cp "/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/reframe/easybuild/OSU-Micro-Benchmarks-7.2-foss-2023b.eb" "/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUEasyBuildCompileTest/OSU-Micro-Benchmarks-7.2-foss-2023b.eb"
echo "DEBUG [Build]: Verifying staged .eb file: $(ls -l /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUEasyBuildCompileTest/OSU-Micro-Benchmarks-7.2-foss-2023b.eb || echo STAGED_EB_NOT_FOUND)"
echo "DEBUG [Build]: Initial loaded modules: $($LMOD_CMD list || echo LMOD_CMD_failed)"
export EASYBUILD_BUILDPATH=/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/build
export EASYBUILD_INSTALLPATH=/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild
export EASYBUILD_PREFIX=/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild
export EASYBUILD_SOURCEPATH=/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/iris/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild
eb OSU-Micro-Benchmarks-7.2-foss-2023b.eb --detect-loaded-modules=warn
