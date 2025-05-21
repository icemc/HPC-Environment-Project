#### Test result
Successfully installed /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/OSU-Micro-Benchmarks-7.2-gompi-2023.09.eb

#### Overview of tested easyconfigs (in order)
 * **SUCCESS** _OSU-Micro-Benchmarks-7.2-gompi-2023.09.eb_ 

#### Time info
 * start: Tue, 20 May 2025 18:54:14 +0000 (UTC)
 * end: Tue, 20 May 2025 18:55:50 +0000 (UTC)

#### EasyBuild info
 * easybuild-framework version: 5.0.0-rd4904b19ad7c067333f8c7679b1b1f1a0512abde
 * easybuild-easyblocks version: 5.0.0-rd4904b19ad7c067333f8c7679b1b1f1a0512abde
 * command line:
```
eb OSU-Micro-Benchmarks-7.2-gompi-2023.09.eb --detect-loaded-modules=warn
```
 * full configuration (includes defaults):
```
--accept-eula-for=''
--allow-loaded-modules='EasyBuild'
--buildpath='/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/build'
--check-ebroot-env-vars='warn'
--cleanup-builddir
--cleanup-easyconfigs
--cleanup-tmpdir
--color='auto'
--container-type='singularity'
--containerpath='/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/containers'
--default-opt-level='defaultopt'
--detect-loaded-modules='warn'
--disable-add-system-to-minimal-toolchains
--disable-allow-modules-tool-mismatch
--disable-allow-unresolved-templates
--disable-allow-use-as-root-and-accept-consequences
--disable-avail-cfgfile-constants
--disable-avail-easyconfig-constants
--disable-avail-easyconfig-licenses
--disable-avail-easyconfig-params
--disable-avail-easyconfig-templates
--disable-avail-hooks
--disable-avail-module-naming-schemes
--disable-avail-modules-tools
--disable-avail-repositories
--disable-backup-patched-files
--disable-check-conflicts
--disable-check-contrib
--disable-check-eb-deps
--disable-check-github
--disable-check-style
--disable-consider-archived-easyconfigs
--disable-container-build-image
--disable-containerize
--disable-copy-ec
--disable-debug
--disable-debug-lmod
--disable-devel
--disable-dry-run
--disable-dry-run-short
--disable-dump-autopep8
--disable-dump-env-script
--disable-enforce-checksums
--disable-experimental
--disable-extended-dry-run
--disable-fail-on-mod-files-gcccore
--disable-fetch
--disable-fix-deprecated-easyconfigs
--disable-force
--disable-group-writable-installdir
--disable-hidden
--disable-ignore-checksums
--disable-ignore-index
--disable-ignore-locks
--disable-ignore-osdeps
--disable-ignore-test-failure
--disable-info
--disable-insecure-download
--disable-install-github-token
--disable-install-latest-eb-release
--disable-job
--disable-keep-debug-symbols
--disable-last-log
--disable-list-toolchains
--disable-logtostdout
--disable-minimal-toolchains
--disable-missing-modules
--disable-module-only
--disable-new-branch-github
--disable-new-pr
--disable-package
--disable-parallel-extensions-install
--disable-pretend
--disable-preview-pr
--disable-quiet
--disable-read-only-installdir
--disable-rebuild
--disable-recursive-module-unload
--disable-regtest
--disable-remove-ghost-install-dirs
--disable-sanity-check-only
--disable-sequential
--disable-set-default-module
--disable-set-gid-bit
--disable-show-config
--disable-show-default-configfiles
--disable-show-default-moduleclasses
--disable-show-ec
--disable-show-full-config
--disable-show-system-info
--disable-silence-hook-trigger
--disable-skip
--disable-skip-extensions
--disable-skip-sanity-check
--disable-skip-test-cases
--disable-skip-test-step
--disable-sticky-bit
--disable-strict-rpath-sanity-check
--disable-terse
--disable-try-ignore-versionsuffixes
--disable-try-update-deps
--disable-unit-testing-mode
--disable-update-modules-tool-cache
--disable-upload-test-report
--disable-use-existing-modules
--disable-verify-easyconfig-filenames
--download-timeout='10'
--env-for-shebang='/usr/bin/env'
--envvars-user-modules='HOME'
--extended-dry-run-ignore-errors
--extra-source-urls=''
--filter-rpath-sanity-libs='libcuda.so,libcuda.so.1,libnvidia-ml.so,libnvidia-ml.so.1'
--fixed-installdir-naming-scheme
--from-pr=''
--generate-devel-module
--ignore-dirs='.git,.svn'
--include-easyblocks-from-pr=''
--include-easyblocks=''
--include-module-naming-schemes=''
--include-toolchains=''
--index-max-age='604800'
--installpath='/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild'
--job-backend='Slurm'
--job-eb-cmd='eb'
--job-max-jobs='0'
--job-max-walltime='24'
--job-output-dir='/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest'
--job-polling-interval='30.0'
--lib-lib64-symlink
--lib64-fallback-sanity-check
--lib64-lib-symlink
--local-var-naming-check='warn'
--logfile-format='easybuild,easybuild-%(name)s-%(version)s-%(date)s.%(time)s.log'
--map-toolchains
--max-fail-ratio-adjust-permissions='0.5'
--max-parallel='16'
--minimal-build-env='CC:gcc,CXX:g++'
--module-depends-on
--module-extensions
--module-naming-scheme='CategorizedModuleNamingScheme'
--module-search-path-headers='cpath'
--module-syntax='Lua'
--moduleclasses='base,ai,astro,bio,cae,chem,compiler,data,debugger,devel,geo,ide,lang,lib,math,mpi,numlib,perf,quantum,phys,system,toolchain,tools,vis'
--modules-tool-version-check
--modules-tool='Lmod'
--mpi-tests
--output-format='txt'
--output-style='auto'
--package-naming-scheme='EasyBuildPNS'
--package-release='1'
--package-tool-options=''
--package-tool='fpm'
--package-type='rpm'
--packagepath='/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/packages'
--pr-target-account='easybuilders'
--pr-target-branch='develop'
--pre-create-installdir
--prefix='/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild'
--repository='FileRepository'
--repositorypath='/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/ebfiles_repo'
--robot-paths=''
--rpath
--search-path-cpp-headers='flags'
--search-path-linker='flags'
--show-progress-bar
--silence-deprecation-warnings=''
--sourcepath='/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild'
--strict='warn'
--subdir-modules='modules'
--subdir-software='software'
--suffix-modules-path='all'
--trace
--use-ccache='False'
--use-f90cache='False'
--wait-on-lock-interval='60'
--wait-on-lock-limit='0'
````

#### System info
 * _core count:_ 1
 * _cpu arch:_ x86_64
 * _cpu arch name:_ UNKNOWN
 * _cpu model:_ AMD EPYC 7H12 64-Core Processor
 * _cpu speed:_ 2600.0
 * _cpu vendor:_ AMD
 * _gcc version:_ Using built-in specs.; COLLECT_GCC=gcc; COLLECT_LTO_WRAPPER=/mnt/aiongpfs/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0/bin/../libexec/gcc/x86_64-pc-linux-gnu/13.2.0/lto-wrapper; OFFLOAD_TARGET_NAMES=nvptx-none; Target: x86_64-pc-linux-gnu; Configured with: ../configure --enable-languages=c,c++,fortran --without-cuda-driver --enable-offload-targets=nvptx-none --enable-lto --enable-checking=release --disable-multilib --enable-shared=yes --enable-static=yes --enable-threads=posix --enable-plugins --enable-gold --enable-ld=default --prefix=/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0 --with-local-prefix=/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0 --enable-bootstrap --with-isl=/tmp/easybuild/iris/2023b/epyc/build/GCCcore/13.2.0/system-system/gcc-13.2.0/stage2_stuff --build=x86_64-pc-linux-gnu --host=x86_64-pc-linux-gnu; Thread model: posix; Supported LTO compression algorithms: zlib zstd; gcc version 13.2.0 (GCC) ; 
 * _glibc version:_ 2.28
 * _hostname:_ aion-0027
 * _os name:_ RHEL
 * _os type:_ Linux
 * _os version:_ 8.10 (Ootpa)
 * _platform name:_ x86_64-unknown-linux
 * _python version:_ 3.11.11 | packaged by conda-forge | (main, Mar  3 2025, 20:43:55) [GCC 13.3.0]
 * _system gcc path:_ /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0/bin/gcc
 * _system python path:_ None
 * _total memory:_ 257207

#### List of loaded modules
 * env/testing/2023b
 * compiler/GCCcore/13.2.0
 * lib/zlib/1.2.13-GCCcore-13.2.0
 * tools/binutils/2.40-GCCcore-13.2.0
 * compiler/GCC/13.2.0
 * tools/numactl/2.0.16-GCCcore-13.2.0
 * tools/XZ/5.4.4-GCCcore-13.2.0
 * lib/libxml2/2.11.5-GCCcore-13.2.0
 * system/libpciaccess/0.17-GCCcore-13.2.0
 * system/hwloc/2.9.2-GCCcore-13.2.0
 * system/OpenSSL/1.1
 * lib/libevent/2.1.12-GCCcore-13.2.0
 * lib/UCX/1.15.0-GCCcore-13.2.0
 * lib/libfabric/1.19.0-GCCcore-13.2.0
 * lib/PMIx/4.2.6-GCCcore-13.2.0
 * lib/UCC/1.2.0-GCCcore-13.2.0
 * mpi/OpenMPI/4.1.6-GCC-13.2.0
 * numlib/OpenBLAS/0.3.24-GCC-13.2.0
 * lib/FlexiBLAS/3.3.1-GCC-13.2.0
 * numlib/FFTW/3.3.10-GCC-13.2.0
 * toolchain/gompi/2023b
 * numlib/FFTW.MPI/3.3.10-gompi-2023b
 * numlib/ScaLAPACK/2.2.0-gompi-2023b-fb
 * toolchain/foss/2023b
 * tools/EasyBuild/5.0.0

#### Environment
```
ACLOCAL_PATH = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/share/aclocal
BASH_ENV = /usr/share/lmod/lmod/init/bash
BASH_FUNC_ml%% = () {  eval "$($LMOD_DIR/ml_cmd "$@")"
}
BASH_FUNC_module%% = () {  if [ -z "${LMOD_SH_DBG_ON+x}" ]; then
 case "$-" in 
 *v*x*)
 __lmod_sh_dbg='vx'
 ;;
 *v*)
 __lmod_sh_dbg='v'
 ;;
 *x*)
 __lmod_sh_dbg='x'
 ;;
 esac;
 fi;
 if [ -n "${__lmod_sh_dbg:-}" ]; then
 set +$__lmod_sh_dbg;
 echo "Shell debugging temporarily silenced: export LMOD_SH_DBG_ON=1 for Lmod's output" 1>&2;
 fi;
 eval "$($LMOD_CMD shell "$@")" && eval "$(${LMOD_SETTARG_CMD:-:} -s sh)";
 __lmod_my_status=$?;
 if [ -n "${__lmod_sh_dbg:-}" ]; then
 echo "Shell debugging restarted" 1>&2;
 set -$__lmod_sh_dbg;
 fi;
 unset __lmod_sh_dbg;
 return $__lmod_my_status
}
BASH_FUNC_which%% = () {  ( alias;
 eval ${which_declare} ) | /usr/bin/which --tty-only --read-alias --read-functions --show-tilde --show-dot $@
}
CMAKE_LIBRARY_PATH = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0/lib64
CMAKE_PREFIX_PATH = /home/users/fkusek/.local/easybuild/software/EasyBuild/5.0.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/ScaLAPACK/2.2.0-gompi-2023b-fb:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW.MPI/3.3.10-gompi-2023b:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenBLAS/0.3.24-GCC-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCC/1.2.0-GCCcore-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libevent/2.1.12-GCCcore-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenSSL/1.1:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libpciaccess/0.17-GCCcore-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0
CPATH = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW.MPI/3.3.10-gompi-2023b/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenBLAS/0.3.24-GCC-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCC/1.2.0-GCCcore-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libevent/2.1.12-GCCcore-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenSSL/1.1/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libpciaccess/0.17-GCCcore-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/include/libxml2:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0/include:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0/include
DBUS_SESSION_BUS_ADDRESS = unix:path=/run/user/490088061/bus
EASYBUILD_BUILDPATH = /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/build
EASYBUILD_INSTALLPATH = /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild
EASYBUILD_MODULES_TOOL = Lmod
EASYBUILD_MODULE_NAMING_SCHEME = CategorizedModuleNamingScheme
EASYBUILD_PREFIX = /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild
EASYBUILD_SOURCEPATH = /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild
EBDEVELBINUTILS = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0/easybuild/tools-binutils-2.40-GCCcore-13.2.0-easybuild-devel
EBDEVELEASYBUILD = /home/users/fkusek/.local/easybuild/software/EasyBuild/5.0.0/easybuild/tools-EasyBuild-5.0.0-easybuild-devel
EBDEVELFFTW = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/easybuild/numlib-FFTW-3.3.10-GCC-13.2.0-easybuild-devel
EBDEVELFFTWMPI = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW.MPI/3.3.10-gompi-2023b/easybuild/numlib-FFTW.MPI-3.3.10-gompi-2023b-easybuild-devel
EBDEVELFLEXIBLAS = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/easybuild/lib-FlexiBLAS-3.3.1-GCC-13.2.0-easybuild-devel
EBDEVELFOSS = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/foss/2023b/easybuild/toolchain-foss-2023b-easybuild-devel
EBDEVELGCC = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCC/13.2.0/easybuild/compiler-GCC-13.2.0-easybuild-devel
EBDEVELGCCCORE = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0/easybuild/compiler-GCCcore-13.2.0-easybuild-devel
EBDEVELGOMPI = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/gompi/2023b/easybuild/toolchain-gompi-2023b-easybuild-devel
EBDEVELHWLOC = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/easybuild/system-hwloc-2.9.2-GCCcore-13.2.0-easybuild-devel
EBDEVELLIBEVENT = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libevent/2.1.12-GCCcore-13.2.0/easybuild/lib-libevent-2.1.12-GCCcore-13.2.0-easybuild-devel
EBDEVELLIBFABRIC = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/easybuild/lib-libfabric-1.19.0-GCCcore-13.2.0-easybuild-devel
EBDEVELLIBPCIACCESS = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libpciaccess/0.17-GCCcore-13.2.0/easybuild/system-libpciaccess-0.17-GCCcore-13.2.0-easybuild-devel
EBDEVELLIBXML2 = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/easybuild/lib-libxml2-2.11.5-GCCcore-13.2.0-easybuild-devel
EBDEVELNUMACTL = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/easybuild/tools-numactl-2.0.16-GCCcore-13.2.0-easybuild-devel
EBDEVELOPENBLAS = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenBLAS/0.3.24-GCC-13.2.0/easybuild/numlib-OpenBLAS-0.3.24-GCC-13.2.0-easybuild-devel
EBDEVELOPENMPI = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/easybuild/mpi-OpenMPI-4.1.6-GCC-13.2.0-easybuild-devel
EBDEVELOPENSSL = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenSSL/1.1/easybuild/system-OpenSSL-1.1-easybuild-devel
EBDEVELPMIX = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/easybuild/lib-PMIx-4.2.6-GCCcore-13.2.0-easybuild-devel
EBDEVELSCALAPACK = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/ScaLAPACK/2.2.0-gompi-2023b-fb/easybuild/numlib-ScaLAPACK-2.2.0-gompi-2023b-fb-easybuild-devel
EBDEVELUCC = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCC/1.2.0-GCCcore-13.2.0/easybuild/lib-UCC-1.2.0-GCCcore-13.2.0-easybuild-devel
EBDEVELUCX = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0/easybuild/lib-UCX-1.15.0-GCCcore-13.2.0-easybuild-devel
EBDEVELXZ = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/easybuild/tools-XZ-5.4.4-GCCcore-13.2.0-easybuild-devel
EBDEVELZLIB = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0/easybuild/lib-zlib-1.2.13-GCCcore-13.2.0-easybuild-devel
EBROOTBINUTILS = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0
EBROOTEASYBUILD = /home/users/fkusek/.local/easybuild/software/EasyBuild/5.0.0
EBROOTFFTW = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0
EBROOTFFTWMPI = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW.MPI/3.3.10-gompi-2023b
EBROOTFLEXIBLAS = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0
EBROOTFOSS = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/foss/2023b
EBROOTGCC = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0
EBROOTGCCCORE = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0
EBROOTGOMPI = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/gompi/2023b
EBROOTHWLOC = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0
EBROOTLIBEVENT = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libevent/2.1.12-GCCcore-13.2.0
EBROOTLIBFABRIC = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0
EBROOTLIBPCIACCESS = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libpciaccess/0.17-GCCcore-13.2.0
EBROOTLIBXML2 = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0
EBROOTNUMACTL = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0
EBROOTOPENBLAS = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenBLAS/0.3.24-GCC-13.2.0
EBROOTOPENMPI = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0
EBROOTOPENSSL = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenSSL/1.1
EBROOTPMIX = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0
EBROOTSCALAPACK = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/ScaLAPACK/2.2.0-gompi-2023b-fb
EBROOTUCC = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCC/1.2.0-GCCcore-13.2.0
EBROOTUCX = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0
EBROOTXZ = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0
EBROOTZLIB = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0
EBVERSIONBINUTILS = 2.40
EBVERSIONEASYBUILD = 5.0.0
EBVERSIONFFTW = 3.3.10
EBVERSIONFFTWMPI = 3.3.10
EBVERSIONFLEXIBLAS = 3.3.1
EBVERSIONFOSS = 2023b
EBVERSIONGCC = 13.2.0
EBVERSIONGCCCORE = 13.2.0
EBVERSIONGOMPI = 2023b
EBVERSIONHWLOC = 2.9.2
EBVERSIONLIBEVENT = 2.1.12
EBVERSIONLIBFABRIC = 1.19.0
EBVERSIONLIBPCIACCESS = 0.17
EBVERSIONLIBXML2 = 2.11.5
EBVERSIONNUMACTL = 2.0.16
EBVERSIONOPENBLAS = 0.3.24
EBVERSIONOPENMPI = 4.1.6
EBVERSIONOPENSSL = 1.1
EBVERSIONPMIX = 4.2.6
EBVERSIONSCALAPACK = 2.2.0
EBVERSIONUCC = 1.2.0
EBVERSIONUCX = 1.15.0
EBVERSIONXZ = 5.4.4
EBVERSIONZLIB = 1.2.13
EB_INSTALLPYTHON = /work/projects/software_set/backup/environments/easybuild/bin/python
EB_SCRIPT_PATH = /home/users/fkusek/.local/easybuild/software/EasyBuild/5.0.0/bin/eb
FANCYLOGGER_IGNORE_MPI4PY = 1
FPATH = /usr/share/lmod/lmod/init/ksh_funcs
HISTCONTROL = ignoredups
HISTSIZE = 1000
HOME = /home/users/fkusek
HOSTNAME = access1.aion-cluster.uni.lux
HYDRA_BOOTSTRAP = slurm
HYDRA_LAUNCHER_EXTRA_ARGS = --external-launcher
I_MPI_HYDRA_BOOTSTRAP = slurm
I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS = --external-launcher
LANG = C.UTF-8
LD_LIBRARY_PATH = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/ScaLAPACK/2.2.0-gompi-2023b-fb/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW.MPI/3.3.10-gompi-2023b/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenBLAS/0.3.24-GCC-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCC/1.2.0-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libevent/2.1.12-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenSSL/1.1/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libpciaccess/0.17-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0/lib64
LESSOPEN = ||/usr/bin/lesspipe.sh %s
LIBRARY_PATH = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/ScaLAPACK/2.2.0-gompi-2023b-fb/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW.MPI/3.3.10-gompi-2023b/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenBLAS/0.3.24-GCC-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCC/1.2.0-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libevent/2.1.12-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenSSL/1.1/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libpciaccess/0.17-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0/lib:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0/lib
LMOD_CMD = /usr/share/lmod/lmod/libexec/lmod
LMOD_DIR = /usr/share/lmod/lmod/libexec
LMOD_FAMILY_ENV = env/testing
LMOD_FAMILY_ENV_VERSION = 2023b
LMOD_PACKAGE_PATH = /opt/sys/etc/lmod-site
LMOD_PKG = /usr/share/lmod/lmod
LMOD_ROOT = /usr/share/lmod
LMOD_SETTARG_FULL_SUPPORT = no
LMOD_SHORT_TIME = 86400
LMOD_SYSTEM_DEFAULT_MODULES = env/release/default
LMOD_VERSION = 8.7.55
LMOD_sys = Linux
LOADEDMODULES = env/testing/2023b:compiler/GCCcore/13.2.0:lib/zlib/1.2.13-GCCcore-13.2.0:tools/binutils/2.40-GCCcore-13.2.0:compiler/GCC/13.2.0:tools/numactl/2.0.16-GCCcore-13.2.0:tools/XZ/5.4.4-GCCcore-13.2.0:lib/libxml2/2.11.5-GCCcore-13.2.0:system/libpciaccess/0.17-GCCcore-13.2.0:system/hwloc/2.9.2-GCCcore-13.2.0:system/OpenSSL/1.1:lib/libevent/2.1.12-GCCcore-13.2.0:lib/UCX/1.15.0-GCCcore-13.2.0:lib/libfabric/1.19.0-GCCcore-13.2.0:lib/PMIx/4.2.6-GCCcore-13.2.0:lib/UCC/1.2.0-GCCcore-13.2.0:mpi/OpenMPI/4.1.6-GCC-13.2.0:numlib/OpenBLAS/0.3.24-GCC-13.2.0:lib/FlexiBLAS/3.3.1-GCC-13.2.0:numlib/FFTW/3.3.10-GCC-13.2.0:toolchain/gompi/2023b:numlib/FFTW.MPI/3.3.10-gompi-2023b:numlib/ScaLAPACK/2.2.0-gompi-2023b-fb:toolchain/foss/2023b:tools/EasyBuild/5.0.0
LOCAL_MODULES = /home/users/fkusek/.local/easybuild/modules/all
LOGNAME = fkusek
LS_COLORS = rs=0:di=38;5;33:ln=38;5;51:mh=00:pi=40;38;5;11:so=38;5;13:do=38;5;5:bd=48;5;232;38;5;11:cd=48;5;232;38;5;3:or=48;5;232;38;5;9:mi=01;05;37;41:su=48;5;196;38;5;15:sg=48;5;11;38;5;16:ca=48;5;196;38;5;226:tw=48;5;10;38;5;16:ow=48;5;10;38;5;21:st=48;5;21;38;5;15:ex=38;5;40:*.tar=38;5;9:*.tgz=38;5;9:*.arc=38;5;9:*.arj=38;5;9:*.taz=38;5;9:*.lha=38;5;9:*.lz4=38;5;9:*.lzh=38;5;9:*.lzma=38;5;9:*.tlz=38;5;9:*.txz=38;5;9:*.tzo=38;5;9:*.t7z=38;5;9:*.zip=38;5;9:*.z=38;5;9:*.dz=38;5;9:*.gz=38;5;9:*.lrz=38;5;9:*.lz=38;5;9:*.lzo=38;5;9:*.xz=38;5;9:*.zst=38;5;9:*.tzst=38;5;9:*.bz2=38;5;9:*.bz=38;5;9:*.tbz=38;5;9:*.tbz2=38;5;9:*.tz=38;5;9:*.deb=38;5;9:*.rpm=38;5;9:*.jar=38;5;9:*.war=38;5;9:*.ear=38;5;9:*.sar=38;5;9:*.rar=38;5;9:*.alz=38;5;9:*.ace=38;5;9:*.zoo=38;5;9:*.cpio=38;5;9:*.7z=38;5;9:*.rz=38;5;9:*.cab=38;5;9:*.wim=38;5;9:*.swm=38;5;9:*.dwm=38;5;9:*.esd=38;5;9:*.jpg=38;5;13:*.jpeg=38;5;13:*.mjpg=38;5;13:*.mjpeg=38;5;13:*.gif=38;5;13:*.bmp=38;5;13:*.pbm=38;5;13:*.pgm=38;5;13:*.ppm=38;5;13:*.tga=38;5;13:*.xbm=38;5;13:*.xpm=38;5;13:*.tif=38;5;13:*.tiff=38;5;13:*.png=38;5;13:*.svg=38;5;13:*.svgz=38;5;13:*.mng=38;5;13:*.pcx=38;5;13:*.mov=38;5;13:*.mpg=38;5;13:*.mpeg=38;5;13:*.m2v=38;5;13:*.mkv=38;5;13:*.webm=38;5;13:*.ogm=38;5;13:*.mp4=38;5;13:*.m4v=38;5;13:*.mp4v=38;5;13:*.vob=38;5;13:*.qt=38;5;13:*.nuv=38;5;13:*.wmv=38;5;13:*.asf=38;5;13:*.rm=38;5;13:*.rmvb=38;5;13:*.flc=38;5;13:*.avi=38;5;13:*.fli=38;5;13:*.flv=38;5;13:*.gl=38;5;13:*.dl=38;5;13:*.xcf=38;5;13:*.xwd=38;5;13:*.yuv=38;5;13:*.cgm=38;5;13:*.emf=38;5;13:*.ogv=38;5;13:*.ogx=38;5;13:*.aac=38;5;45:*.au=38;5;45:*.flac=38;5;45:*.m4a=38;5;45:*.mid=38;5;45:*.midi=38;5;45:*.mka=38;5;45:*.mp3=38;5;45:*.mpc=38;5;45:*.ogg=38;5;45:*.ra=38;5;45:*.wav=38;5;45:*.oga=38;5;45:*.opus=38;5;45:*.spx=38;5;45:*.xspf=38;5;45:
MAIL = /var/spool/mail/fkusek
MANPATH = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/share/man:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/share/man:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/share/man:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/share/man:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/share/man:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/share/man:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/share/man:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/share/man:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/share/man:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0/share/man:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0/share/man:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0/share/man:/usr/share/lmod/lmod/share/man::/opt/puppetlabs/puppet/share/man
MODULEPATH = /home/users/fkusek/.local/easybuild/modules/all:/mnt/aiongpfs/users/fkusek/work/projects/software_set/easybuild/binary/2023b/modules/all:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all:/opt/apps/easybuild/environment/modules:/cvmfs/software.eessi.io/init/modules:/opt/apps/easybuild/systems/aion/rhel810-20250405/2023b/epyc/modules/all:/opt/apps/easybuild/systems/binary/rhel810-20250405/2023b/generic/modules/all
MODULEPATH_ROOT = /usr/share/modulefiles
MODULESHOME = /usr/share/lmod/lmod
NODECLASS = epyc
OLDPWD = /home/users/fkusek/HPC-Environment-Project/reframe
OMPI_MCA_plm_slurm_args = --external-launcher
PATH = /home/users/fkusek/.local/easybuild/software/EasyBuild/5.0.0/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCC/1.2.0-GCCcore-13.2.0/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libevent/2.1.12-GCCcore-13.2.0/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenSSL/1.1/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/sbin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0/bin:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0/bin:/home/users/fkusek/.local/bin:/home/users/fkusek/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/puppetlabs/bin:/usr/share/lmod/lmod/libexec
PKG_CONFIG_PATH = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/ScaLAPACK/2.2.0-gompi-2023b-fb/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenBLAS/0.3.24-GCC-13.2.0/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libevent/2.1.12-GCCcore-13.2.0/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenSSL/1.1/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libpciaccess/0.17-GCCcore-13.2.0/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/lib/pkgconfig:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0/lib/pkgconfig
PROJECTHOME = /work/projects/
PROJECTSCRATCH = /scratch/projects/
PROJECTWORK = /work/projects/
PRTE_MCA_plm_slurm_args = --external-launcher
PWD = /mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest
PYTHONOPTIMIZE = 1
PYTHONPATH = /home/users/fkusek/.local/easybuild/software/EasyBuild/5.0.0/lib/python3.11/site-packages
RESIF_ARCH = epyc
RFM_INSTALL_PREFIX = /opt/apps/easybuild/systems/aion/rhel810-20250405/2023b/epyc/software/ReFrame/4.7.4-GCCcore-13.2.0/lib/python3.11/site-packages
SCRATCH = /scratch/users/fkusek/
SELINUX_LEVEL_REQUESTED = 
SELINUX_ROLE_REQUESTED = 
SELINUX_USE_CURRENT_RANGE = 
SHELL = /bin/bash
SHLVL = 4
SLURMD_DEBUG = 2
SLURMD_NODENAME = aion-0027
SLURM_CLUSTER_NAME = aion
SLURM_CONF = /etc/slurm/slurm.conf
SLURM_CPUS_ON_NODE = 1
SLURM_GTIDS = 0
SLURM_JOBID = 8170820
SLURM_JOB_ACCOUNT = students
SLURM_JOB_CPUS_PER_NODE = 1
SLURM_JOB_END_TIME = 1747768960
SLURM_JOB_GID = 666
SLURM_JOB_ID = 8170820
SLURM_JOB_NAME = interactive
SLURM_JOB_NODELIST = aion-0027
SLURM_JOB_NUM_NODES = 1
SLURM_JOB_PARTITION = interactive
SLURM_JOB_QOS = debug
SLURM_JOB_START_TIME = 1747767160
SLURM_JOB_UID = 490088061
SLURM_JOB_USER = fkusek
SLURM_LAUNCH_NODE_IPADDR = 172.21.2.13
SLURM_LOCALID = 0
SLURM_MPI_TYPE = pmix
SLURM_NNODES = 1
SLURM_NODEID = 0
SLURM_NODELIST = aion-0027
SLURM_PMIXP_ABORT_AGENT_PORT = 44153
SLURM_PMIX_MAPPING_SERV = (vector,(0,1,1))
SLURM_PRIO_PROCESS = 0
SLURM_PROCID = 0
SLURM_PTY_PORT = 44152
SLURM_PTY_WIN_COL = 144
SLURM_PTY_WIN_ROW = 38
SLURM_SRUN_COMM_HOST = 172.21.2.13
SLURM_SRUN_COMM_PORT = 44154
SLURM_STEPID = 4294967290
SLURM_STEP_ID = 4294967290
SLURM_STEP_LAUNCHER_PORT = 44154
SLURM_STEP_NODELIST = aion-0027
SLURM_STEP_NUM_NODES = 1
SLURM_STEP_NUM_TASKS = 1
SLURM_STEP_TASKS_PER_NODE = 1
SLURM_SUBMIT_DIR = /mnt/aiongpfs/users/fkusek
SLURM_SUBMIT_HOST = access1.aion-cluster.uni.lux
SLURM_TASKS_PER_NODE = 1
SLURM_TASK_PID = 2579235
SLURM_TOPOLOGY_ADDR = aib-switch-[1-4].aib-switch-6.aion-0027
SLURM_TOPOLOGY_ADDR_PATTERN = switch.switch.node
SPRIO_FORMAT = %.10i %9r %.8u %.10Y %.10A %.10F %.10P %.10Q
SQUEUE_FORMAT = %.8i %.6P %.9q %.20j %.10u %.4D %.5C %.2t %.12M %.12L %.8Q %R
SRUN_DEBUG = 3
SSH_CLIENT = 195.46.241.162 51972 8022
SSH_CONNECTION = 195.46.241.162 51972 172.20.3.16 8022
SSH_TTY = /dev/pts/113
S_COLORS = auto
TERM = xterm-256color
TMPDIR = /tmp
ULHPC_CLUSTER = aion
USER = fkusek
XDG_DATA_DIRS = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/share:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/share:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/share:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/share:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/share:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0/share:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/share:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/share:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/share:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/share:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0/share:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0/share:/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0/share
XDG_RUNTIME_DIR = /run/user/490088061
XDG_SESSION_ID = 2988167
_ = /work/projects/software_set/backup/environments/easybuild/bin/python
_LMFILES_ = /opt/apps/easybuild/environment/modules/env/testing/2023b.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/compiler/GCCcore/13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/lib/zlib/1.2.13-GCCcore-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/tools/binutils/2.40-GCCcore-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/compiler/GCC/13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/tools/numactl/2.0.16-GCCcore-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/tools/XZ/5.4.4-GCCcore-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/lib/libxml2/2.11.5-GCCcore-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/system/libpciaccess/0.17-GCCcore-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/system/hwloc/2.9.2-GCCcore-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/system/OpenSSL/1.1.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/lib/libevent/2.1.12-GCCcore-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/lib/UCX/1.15.0-GCCcore-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/lib/libfabric/1.19.0-GCCcore-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/lib/PMIx/4.2.6-GCCcore-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/lib/UCC/1.2.0-GCCcore-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/mpi/OpenMPI/4.1.6-GCC-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/numlib/OpenBLAS/0.3.24-GCC-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/lib/FlexiBLAS/3.3.1-GCC-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/numlib/FFTW/3.3.10-GCC-13.2.0.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/toolchain/gompi/2023b.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/numlib/FFTW.MPI/3.3.10-gompi-2023b.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/numlib/ScaLAPACK/2.2.0-gompi-2023b-fb.lua:/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all/toolchain/foss/2023b.lua:/home/users/fkusek/.local/easybuild/modules/all/tools/EasyBuild/5.0.0.lua
_ModuleTable001_ = X01vZHVsZVRhYmxlXyA9IHsKTVR2ZXJzaW9uID0gMywKY19yZWJ1aWxkVGltZSA9IGZhbHNlLApjX3Nob3J0VGltZSA9IGZhbHNlLApkZXB0aFQgPSB7fSwKZmFtaWx5ID0gewplbnYgPSAiZW52L3Rlc3RpbmciLAp9LAptVCA9IHsKWyJjb21waWxlci9HQ0MiXSA9IHsKZm4gPSAiL3dvcmsvcHJvamVjdHMvc29mdHdhcmVfc2V0L2Vhc3lidWlsZC9haW9uLzIwMjNiL2VweWMvbW9kdWxlcy9hbGwvY29tcGlsZXIvR0NDLzEzLjIuMC5sdWEiLApmdWxsTmFtZSA9ICJjb21waWxlci9HQ0MvMTMuMi4wIiwKbG9hZE9yZGVyID0gNSwKcHJvcFQgPSB7fSwKc3RhY2tEZXB0aCA9IDEsCnN0YXR1cyA9ICJhY3RpdmUiLAp1c2VyTmFtZSA9ICJjb21waWxlci9HQ0MvMTMuMi4wIiwKd1Yg
_ModuleTable002_ = PSAiMDAwMDAwMDEzLjAwMDAwMDAwMi4qemZpbmFsIiwKfSwKWyJjb21waWxlci9HQ0Njb3JlIl0gPSB7CmZuID0gIi93b3JrL3Byb2plY3RzL3NvZnR3YXJlX3NldC9lYXN5YnVpbGQvYWlvbi8yMDIzYi9lcHljL21vZHVsZXMvYWxsL2NvbXBpbGVyL0dDQ2NvcmUvMTMuMi4wLmx1YSIsCmZ1bGxOYW1lID0gImNvbXBpbGVyL0dDQ2NvcmUvMTMuMi4wIiwKbG9hZE9yZGVyID0gMiwKcHJvcFQgPSB7fSwKc3RhY2tEZXB0aCA9IDIsCnN0YXR1cyA9ICJhY3RpdmUiLAp1c2VyTmFtZSA9ICJjb21waWxlci9HQ0Njb3JlLzEzLjIuMCIsCndWID0gIjAwMDAwMDAxMy4wMDAwMDAwMDIuKnpmaW5hbCIsCn0sClsiZW52L3Rlc3RpbmciXSA9IHsKYWN0aW9uQSA9IHsKCiJhcHBlbmRfcGF0
_ModuleTable003_ = aChcIk1PRFVMRVBBVEhcIixcIi9vcHQvYXBwcy9lYXN5YnVpbGQvc3lzdGVtcy8vYWlvbi9yaGVsODEwLTIwMjUwNDA1LzIwMjNiL2VweWMvbW9kdWxlcy9hbGxcIikiLCAiYXBwZW5kX3BhdGgoXCJNT0RVTEVQQVRIXCIsXCIvb3B0L2FwcHMvZWFzeWJ1aWxkL3N5c3RlbXMvL2JpbmFyeS9yaGVsODEwLTIwMjUwNDA1LzIwMjNiL2dlbmVyaWMvbW9kdWxlcy9hbGxcIikiLAp9LApmbiA9ICIvb3B0L2FwcHMvZWFzeWJ1aWxkL2Vudmlyb25tZW50L21vZHVsZXMvZW52L3Rlc3RpbmcvMjAyM2IubHVhIiwKZnVsbE5hbWUgPSAiZW52L3Rlc3RpbmcvMjAyM2IiLApsb2FkT3JkZXIgPSAxLApwcm9wVCA9IHsKbG1vZCA9IHsKc3RpY2t5ID0gMSwKfSwKfSwKc3RhY2tEZXB0aCA9IDAs
_ModuleTable004_ = CnN0YXR1cyA9ICJhY3RpdmUiLAp1c2VyTmFtZSA9ICJlbnYvdGVzdGluZy8yMDIzYiIsCndWID0gIjAwMDAwMjAyMy4qYi4qemZpbmFsIiwKfSwKWyJsaWIvRmxleGlCTEFTIl0gPSB7CmZuID0gIi93b3JrL3Byb2plY3RzL3NvZnR3YXJlX3NldC9lYXN5YnVpbGQvYWlvbi8yMDIzYi9lcHljL21vZHVsZXMvYWxsL2xpYi9GbGV4aUJMQVMvMy4zLjEtR0NDLTEzLjIuMC5sdWEiLApmdWxsTmFtZSA9ICJsaWIvRmxleGlCTEFTLzMuMy4xLUdDQy0xMy4yLjAiLApsb2FkT3JkZXIgPSAxOSwKcHJvcFQgPSB7fSwKc3RhY2tEZXB0aCA9IDEsCnN0YXR1cyA9ICJhY3RpdmUiLAp1c2VyTmFtZSA9ICJsaWIvRmxleGlCTEFTLzMuMy4xLUdDQy0xMy4yLjAiLAp3ViA9ICIwMDAwMDAwMDMu
_ModuleTable005_ = MDAwMDAwMDAzLjAwMDAwMDAwMS4qZ2NjLip6ZmluYWwtLjAwMDAwMDAxMy4wMDAwMDAwMDIuKnpmaW5hbCIsCn0sClsibGliL1BNSXgiXSA9IHsKZm4gPSAiL3dvcmsvcHJvamVjdHMvc29mdHdhcmVfc2V0L2Vhc3lidWlsZC9haW9uLzIwMjNiL2VweWMvbW9kdWxlcy9hbGwvbGliL1BNSXgvNC4yLjYtR0NDY29yZS0xMy4yLjAubHVhIiwKZnVsbE5hbWUgPSAibGliL1BNSXgvNC4yLjYtR0NDY29yZS0xMy4yLjAiLApsb2FkT3JkZXIgPSAxNSwKcHJvcFQgPSB7fSwKc3RhY2tEZXB0aCA9IDIsCnN0YXR1cyA9ICJhY3RpdmUiLAp1c2VyTmFtZSA9ICJsaWIvUE1JeC80LjIuNi1HQ0Njb3JlLTEzLjIuMCIsCndWID0gIjAwMDAwMDAwNC4wMDAwMDAwMDIuMDAwMDAwMDA2LipnY2Nj
_ModuleTable006_ = b3JlLip6ZmluYWwtLjAwMDAwMDAxMy4wMDAwMDAwMDIuKnpmaW5hbCIsCn0sClsibGliL1VDQyJdID0gewpmbiA9ICIvd29yay9wcm9qZWN0cy9zb2Z0d2FyZV9zZXQvZWFzeWJ1aWxkL2Fpb24vMjAyM2IvZXB5Yy9tb2R1bGVzL2FsbC9saWIvVUNDLzEuMi4wLUdDQ2NvcmUtMTMuMi4wLmx1YSIsCmZ1bGxOYW1lID0gImxpYi9VQ0MvMS4yLjAtR0NDY29yZS0xMy4yLjAiLApsb2FkT3JkZXIgPSAxNiwKcHJvcFQgPSB7fSwKc3RhY2tEZXB0aCA9IDIsCnN0YXR1cyA9ICJhY3RpdmUiLAp1c2VyTmFtZSA9ICJsaWIvVUNDLzEuMi4wLUdDQ2NvcmUtMTMuMi4wIiwKd1YgPSAiMDAwMDAwMDAxLjAwMDAwMDAwMi4qZ2NjY29yZS4qemZpbmFsLS4wMDAwMDAwMTMuMDAwMDAwMDAyLip6
_ModuleTable007_ = ZmluYWwiLAp9LApbImxpYi9VQ1giXSA9IHsKZm4gPSAiL3dvcmsvcHJvamVjdHMvc29mdHdhcmVfc2V0L2Vhc3lidWlsZC9haW9uLzIwMjNiL2VweWMvbW9kdWxlcy9hbGwvbGliL1VDWC8xLjE1LjAtR0NDY29yZS0xMy4yLjAubHVhIiwKZnVsbE5hbWUgPSAibGliL1VDWC8xLjE1LjAtR0NDY29yZS0xMy4yLjAiLApsb2FkT3JkZXIgPSAxMywKcHJvcFQgPSB7fSwKc3RhY2tEZXB0aCA9IDIsCnN0YXR1cyA9ICJhY3RpdmUiLAp1c2VyTmFtZSA9ICJsaWIvVUNYLzEuMTUuMC1HQ0Njb3JlLTEzLjIuMCIsCndWID0gIjAwMDAwMDAwMS4wMDAwMDAwMTUuKmdjY2NvcmUuKnpmaW5hbC0uMDAwMDAwMDEzLjAwMDAwMDAwMi4qemZpbmFsIiwKfSwKWyJsaWIvbGliZXZlbnQiXSA9IHsK
_ModuleTable008_ = Zm4gPSAiL3dvcmsvcHJvamVjdHMvc29mdHdhcmVfc2V0L2Vhc3lidWlsZC9haW9uLzIwMjNiL2VweWMvbW9kdWxlcy9hbGwvbGliL2xpYmV2ZW50LzIuMS4xMi1HQ0Njb3JlLTEzLjIuMC5sdWEiLApmdWxsTmFtZSA9ICJsaWIvbGliZXZlbnQvMi4xLjEyLUdDQ2NvcmUtMTMuMi4wIiwKbG9hZE9yZGVyID0gMTIsCnByb3BUID0ge30sCnN0YWNrRGVwdGggPSAyLApzdGF0dXMgPSAiYWN0aXZlIiwKdXNlck5hbWUgPSAibGliL2xpYmV2ZW50LzIuMS4xMi1HQ0Njb3JlLTEzLjIuMCIsCndWID0gIjAwMDAwMDAwMi4wMDAwMDAwMDEuMDAwMDAwMDEyLipnY2Njb3JlLip6ZmluYWwtLjAwMDAwMDAxMy4wMDAwMDAwMDIuKnpmaW5hbCIsCn0sClsibGliL2xpYmZhYnJpYyJdID0gewpm
_ModuleTable009_ = biA9ICIvd29yay9wcm9qZWN0cy9zb2Z0d2FyZV9zZXQvZWFzeWJ1aWxkL2Fpb24vMjAyM2IvZXB5Yy9tb2R1bGVzL2FsbC9saWIvbGliZmFicmljLzEuMTkuMC1HQ0Njb3JlLTEzLjIuMC5sdWEiLApmdWxsTmFtZSA9ICJsaWIvbGliZmFicmljLzEuMTkuMC1HQ0Njb3JlLTEzLjIuMCIsCmxvYWRPcmRlciA9IDE0LApwcm9wVCA9IHt9LApzdGFja0RlcHRoID0gMiwKc3RhdHVzID0gImFjdGl2ZSIsCnVzZXJOYW1lID0gImxpYi9saWJmYWJyaWMvMS4xOS4wLUdDQ2NvcmUtMTMuMi4wIiwKd1YgPSAiMDAwMDAwMDAxLjAwMDAwMDAxOS4qZ2NjY29yZS4qemZpbmFsLS4wMDAwMDAwMTMuMDAwMDAwMDAyLip6ZmluYWwiLAp9LApbImxpYi9saWJ4bWwyIl0gPSB7CmZuID0gIi93b3Jr
_ModuleTable010_ = L3Byb2plY3RzL3NvZnR3YXJlX3NldC9lYXN5YnVpbGQvYWlvbi8yMDIzYi9lcHljL21vZHVsZXMvYWxsL2xpYi9saWJ4bWwyLzIuMTEuNS1HQ0Njb3JlLTEzLjIuMC5sdWEiLApmdWxsTmFtZSA9ICJsaWIvbGlieG1sMi8yLjExLjUtR0NDY29yZS0xMy4yLjAiLApsb2FkT3JkZXIgPSA4LApwcm9wVCA9IHt9LApzdGFja0RlcHRoID0gMywKc3RhdHVzID0gImFjdGl2ZSIsCnVzZXJOYW1lID0gImxpYi9saWJ4bWwyLzIuMTEuNS1HQ0Njb3JlLTEzLjIuMCIsCndWID0gIjAwMDAwMDAwMi4wMDAwMDAwMTEuMDAwMDAwMDA1LipnY2Njb3JlLip6ZmluYWwtLjAwMDAwMDAxMy4wMDAwMDAwMDIuKnpmaW5hbCIsCn0sClsibGliL3psaWIiXSA9IHsKZm4gPSAiL3dvcmsvcHJvamVjdHMv
_ModuleTable011_ = c29mdHdhcmVfc2V0L2Vhc3lidWlsZC9haW9uLzIwMjNiL2VweWMvbW9kdWxlcy9hbGwvbGliL3psaWIvMS4yLjEzLUdDQ2NvcmUtMTMuMi4wLmx1YSIsCmZ1bGxOYW1lID0gImxpYi96bGliLzEuMi4xMy1HQ0Njb3JlLTEzLjIuMCIsCmxvYWRPcmRlciA9IDMsCnByb3BUID0ge30sCnN0YWNrRGVwdGggPSAzLApzdGF0dXMgPSAiYWN0aXZlIiwKdXNlck5hbWUgPSAibGliL3psaWIvMS4yLjEzLUdDQ2NvcmUtMTMuMi4wIiwKd1YgPSAiMDAwMDAwMDAxLjAwMDAwMDAwMi4wMDAwMDAwMTMuKmdjY2NvcmUuKnpmaW5hbC0uMDAwMDAwMDEzLjAwMDAwMDAwMi4qemZpbmFsIiwKfSwKWyJtcGkvT3Blbk1QSSJdID0gewpmbiA9ICIvd29yay9wcm9qZWN0cy9zb2Z0d2FyZV9zZXQvZWFz
_ModuleTable012_ = eWJ1aWxkL2Fpb24vMjAyM2IvZXB5Yy9tb2R1bGVzL2FsbC9tcGkvT3Blbk1QSS80LjEuNi1HQ0MtMTMuMi4wLmx1YSIsCmZ1bGxOYW1lID0gIm1waS9PcGVuTVBJLzQuMS42LUdDQy0xMy4yLjAiLApsb2FkT3JkZXIgPSAxNywKcHJvcFQgPSB7fSwKc3RhY2tEZXB0aCA9IDEsCnN0YXR1cyA9ICJhY3RpdmUiLAp1c2VyTmFtZSA9ICJtcGkvT3Blbk1QSS80LjEuNi1HQ0MtMTMuMi4wIiwKd1YgPSAiMDAwMDAwMDA0LjAwMDAwMDAwMS4wMDAwMDAwMDYuKmdjYy4qemZpbmFsLS4wMDAwMDAwMTMuMDAwMDAwMDAyLip6ZmluYWwiLAp9LApbIm51bWxpYi9GRlRXIl0gPSB7CmZuID0gIi93b3JrL3Byb2plY3RzL3NvZnR3YXJlX3NldC9lYXN5YnVpbGQvYWlvbi8yMDIzYi9lcHljL21v
_ModuleTable013_ = ZHVsZXMvYWxsL251bWxpYi9GRlRXLzMuMy4xMC1HQ0MtMTMuMi4wLmx1YSIsCmZ1bGxOYW1lID0gIm51bWxpYi9GRlRXLzMuMy4xMC1HQ0MtMTMuMi4wIiwKbG9hZE9yZGVyID0gMjAsCnByb3BUID0ge30sCnN0YWNrRGVwdGggPSAxLApzdGF0dXMgPSAiYWN0aXZlIiwKdXNlck5hbWUgPSAibnVtbGliL0ZGVFcvMy4zLjEwLUdDQy0xMy4yLjAiLAp3ViA9ICIwMDAwMDAwMDMuMDAwMDAwMDAzLjAwMDAwMDAxMC4qZ2NjLip6ZmluYWwtLjAwMDAwMDAxMy4wMDAwMDAwMDIuKnpmaW5hbCIsCn0sClsibnVtbGliL0ZGVFcuTVBJIl0gPSB7CmZuID0gIi93b3JrL3Byb2plY3RzL3NvZnR3YXJlX3NldC9lYXN5YnVpbGQvYWlvbi8yMDIzYi9lcHljL21vZHVsZXMvYWxsL251bWxpYi9G
_ModuleTable014_ = RlRXLk1QSS8zLjMuMTAtZ29tcGktMjAyM2IubHVhIiwKZnVsbE5hbWUgPSAibnVtbGliL0ZGVFcuTVBJLzMuMy4xMC1nb21waS0yMDIzYiIsCmxvYWRPcmRlciA9IDIyLApwcm9wVCA9IHt9LApzdGFja0RlcHRoID0gMSwKc3RhdHVzID0gImFjdGl2ZSIsCnVzZXJOYW1lID0gIm51bWxpYi9GRlRXLk1QSS8zLjMuMTAtZ29tcGktMjAyM2IiLAp3ViA9ICIwMDAwMDAwMDMuMDAwMDAwMDAzLjAwMDAwMDAxMC4qZ29tcGkuKnpmaW5hbC0uMDAwMDAyMDIzLipiLip6ZmluYWwiLAp9LApbIm51bWxpYi9PcGVuQkxBUyJdID0gewpmbiA9ICIvd29yay9wcm9qZWN0cy9zb2Z0d2FyZV9zZXQvZWFzeWJ1aWxkL2Fpb24vMjAyM2IvZXB5Yy9tb2R1bGVzL2FsbC9udW1saWIvT3BlbkJMQVMv
_ModuleTable015_ = MC4zLjI0LUdDQy0xMy4yLjAubHVhIiwKZnVsbE5hbWUgPSAibnVtbGliL09wZW5CTEFTLzAuMy4yNC1HQ0MtMTMuMi4wIiwKbG9hZE9yZGVyID0gMTgsCnByb3BUID0ge30sCnN0YWNrRGVwdGggPSAyLApzdGF0dXMgPSAiYWN0aXZlIiwKdXNlck5hbWUgPSAibnVtbGliL09wZW5CTEFTLzAuMy4yNC1HQ0MtMTMuMi4wIiwKd1YgPSAiMDAwMDAwMDAwLjAwMDAwMDAwMy4wMDAwMDAwMjQuKmdjYy4qemZpbmFsLS4wMDAwMDAwMTMuMDAwMDAwMDAyLip6ZmluYWwiLAp9LApbIm51bWxpYi9TY2FMQVBBQ0siXSA9IHsKZm4gPSAiL3dvcmsvcHJvamVjdHMvc29mdHdhcmVfc2V0L2Vhc3lidWlsZC9haW9uLzIwMjNiL2VweWMvbW9kdWxlcy9hbGwvbnVtbGliL1NjYUxBUEFDSy8yLjIu
_ModuleTable016_ = MC1nb21waS0yMDIzYi1mYi5sdWEiLApmdWxsTmFtZSA9ICJudW1saWIvU2NhTEFQQUNLLzIuMi4wLWdvbXBpLTIwMjNiLWZiIiwKbG9hZE9yZGVyID0gMjMsCnByb3BUID0ge30sCnN0YWNrRGVwdGggPSAxLApzdGF0dXMgPSAiYWN0aXZlIiwKdXNlck5hbWUgPSAibnVtbGliL1NjYUxBUEFDSy8yLjIuMC1nb21waS0yMDIzYi1mYiIsCndWID0gIjAwMDAwMDAwMi4wMDAwMDAwMDIuKmdvbXBpLip6ZmluYWwtLjAwMDAwMjAyMy4qYi4qZmIuKnpmaW5hbCIsCn0sClsic3lzdGVtL09wZW5TU0wiXSA9IHsKZm4gPSAiL3dvcmsvcHJvamVjdHMvc29mdHdhcmVfc2V0L2Vhc3lidWlsZC9haW9uLzIwMjNiL2VweWMvbW9kdWxlcy9hbGwvc3lzdGVtL09wZW5TU0wvMS4xLmx1YSIsCmZ1
_ModuleTable017_ = bGxOYW1lID0gInN5c3RlbS9PcGVuU1NMLzEuMSIsCmxvYWRPcmRlciA9IDExLApwcm9wVCA9IHt9LApzdGFja0RlcHRoID0gMywKc3RhdHVzID0gImFjdGl2ZSIsCnVzZXJOYW1lID0gInN5c3RlbS9PcGVuU1NMLzEuMSIsCndWID0gIjAwMDAwMDAwMS4wMDAwMDAwMDEuKnpmaW5hbCIsCn0sClsic3lzdGVtL2h3bG9jIl0gPSB7CmZuID0gIi93b3JrL3Byb2plY3RzL3NvZnR3YXJlX3NldC9lYXN5YnVpbGQvYWlvbi8yMDIzYi9lcHljL21vZHVsZXMvYWxsL3N5c3RlbS9od2xvYy8yLjkuMi1HQ0Njb3JlLTEzLjIuMC5sdWEiLApmdWxsTmFtZSA9ICJzeXN0ZW0vaHdsb2MvMi45LjItR0NDY29yZS0xMy4yLjAiLApsb2FkT3JkZXIgPSAxMCwKcHJvcFQgPSB7fSwKc3RhY2tEZXB0
_ModuleTable018_ = aCA9IDIsCnN0YXR1cyA9ICJhY3RpdmUiLAp1c2VyTmFtZSA9ICJzeXN0ZW0vaHdsb2MvMi45LjItR0NDY29yZS0xMy4yLjAiLAp3ViA9ICIwMDAwMDAwMDIuMDAwMDAwMDA5LjAwMDAwMDAwMi4qZ2NjY29yZS4qemZpbmFsLS4wMDAwMDAwMTMuMDAwMDAwMDAyLip6ZmluYWwiLAp9LApbInN5c3RlbS9saWJwY2lhY2Nlc3MiXSA9IHsKZm4gPSAiL3dvcmsvcHJvamVjdHMvc29mdHdhcmVfc2V0L2Vhc3lidWlsZC9haW9uLzIwMjNiL2VweWMvbW9kdWxlcy9hbGwvc3lzdGVtL2xpYnBjaWFjY2Vzcy8wLjE3LUdDQ2NvcmUtMTMuMi4wLmx1YSIsCmZ1bGxOYW1lID0gInN5c3RlbS9saWJwY2lhY2Nlc3MvMC4xNy1HQ0Njb3JlLTEzLjIuMCIsCmxvYWRPcmRlciA9IDksCnByb3BUID0g
_ModuleTable019_ = e30sCnN0YWNrRGVwdGggPSAzLApzdGF0dXMgPSAiYWN0aXZlIiwKdXNlck5hbWUgPSAic3lzdGVtL2xpYnBjaWFjY2Vzcy8wLjE3LUdDQ2NvcmUtMTMuMi4wIiwKd1YgPSAiMDAwMDAwMDAwLjAwMDAwMDAxNy4qZ2NjY29yZS4qemZpbmFsLS4wMDAwMDAwMTMuMDAwMDAwMDAyLip6ZmluYWwiLAp9LApbInRvb2xjaGFpbi9mb3NzIl0gPSB7CmZuID0gIi93b3JrL3Byb2plY3RzL3NvZnR3YXJlX3NldC9lYXN5YnVpbGQvYWlvbi8yMDIzYi9lcHljL21vZHVsZXMvYWxsL3Rvb2xjaGFpbi9mb3NzLzIwMjNiLmx1YSIsCmZ1bGxOYW1lID0gInRvb2xjaGFpbi9mb3NzLzIwMjNiIiwKbG9hZE9yZGVyID0gMjQsCnByb3BUID0ge30sCnN0YWNrRGVwdGggPSAwLApzdGF0dXMgPSAiYWN0
_ModuleTable020_ = aXZlIiwKdXNlck5hbWUgPSAidG9vbGNoYWluL2Zvc3MvMjAyM2IiLAp3ViA9ICIwMDAwMDIwMjMuKmIuKnpmaW5hbCIsCn0sClsidG9vbGNoYWluL2dvbXBpIl0gPSB7CmZuID0gIi93b3JrL3Byb2plY3RzL3NvZnR3YXJlX3NldC9lYXN5YnVpbGQvYWlvbi8yMDIzYi9lcHljL21vZHVsZXMvYWxsL3Rvb2xjaGFpbi9nb21waS8yMDIzYi5sdWEiLApmdWxsTmFtZSA9ICJ0b29sY2hhaW4vZ29tcGkvMjAyM2IiLApsb2FkT3JkZXIgPSAyMSwKcHJvcFQgPSB7fSwKc3RhY2tEZXB0aCA9IDIsCnN0YXR1cyA9ICJhY3RpdmUiLAp1c2VyTmFtZSA9ICJ0b29sY2hhaW4vZ29tcGkvMjAyM2IiLAp3ViA9ICIwMDAwMDIwMjMuKmIuKnpmaW5hbCIsCn0sClsidG9vbHMvRWFzeUJ1aWxkIl0g
_ModuleTable021_ = PSB7CmZuID0gIi9ob21lL3VzZXJzL2ZrdXNlay8ubG9jYWwvZWFzeWJ1aWxkL21vZHVsZXMvYWxsL3Rvb2xzL0Vhc3lCdWlsZC81LjAuMC5sdWEiLApmdWxsTmFtZSA9ICJ0b29scy9FYXN5QnVpbGQvNS4wLjAiLApsb2FkT3JkZXIgPSAyNSwKcHJvcFQgPSB7fSwKc3RhY2tEZXB0aCA9IDAsCnN0YXR1cyA9ICJhY3RpdmUiLAp1c2VyTmFtZSA9ICJ0b29scy9FYXN5QnVpbGQiLAp3ViA9ICIwMDAwMDAwMDUuKnpmaW5hbCIsCn0sClsidG9vbHMvWFoiXSA9IHsKZm4gPSAiL3dvcmsvcHJvamVjdHMvc29mdHdhcmVfc2V0L2Vhc3lidWlsZC9haW9uLzIwMjNiL2VweWMvbW9kdWxlcy9hbGwvdG9vbHMvWFovNS40LjQtR0NDY29yZS0xMy4yLjAubHVhIiwKZnVsbE5hbWUgPSAidG9v
_ModuleTable022_ = bHMvWFovNS40LjQtR0NDY29yZS0xMy4yLjAiLApsb2FkT3JkZXIgPSA3LApwcm9wVCA9IHt9LApzdGFja0RlcHRoID0gNCwKc3RhdHVzID0gImFjdGl2ZSIsCnVzZXJOYW1lID0gInRvb2xzL1haLzUuNC40LUdDQ2NvcmUtMTMuMi4wIiwKd1YgPSAiMDAwMDAwMDA1LjAwMDAwMDAwNC4wMDAwMDAwMDQuKmdjY2NvcmUuKnpmaW5hbC0uMDAwMDAwMDEzLjAwMDAwMDAwMi4qemZpbmFsIiwKfSwKWyJ0b29scy9iaW51dGlscyJdID0gewpmbiA9ICIvd29yay9wcm9qZWN0cy9zb2Z0d2FyZV9zZXQvZWFzeWJ1aWxkL2Fpb24vMjAyM2IvZXB5Yy9tb2R1bGVzL2FsbC90b29scy9iaW51dGlscy8yLjQwLUdDQ2NvcmUtMTMuMi4wLmx1YSIsCmZ1bGxOYW1lID0gInRvb2xzL2JpbnV0aWxz
_ModuleTable023_ = LzIuNDAtR0NDY29yZS0xMy4yLjAiLApsb2FkT3JkZXIgPSA0LApwcm9wVCA9IHt9LApzdGFja0RlcHRoID0gMiwKc3RhdHVzID0gImFjdGl2ZSIsCnVzZXJOYW1lID0gInRvb2xzL2JpbnV0aWxzLzIuNDAtR0NDY29yZS0xMy4yLjAiLAp3ViA9ICIwMDAwMDAwMDIuMDAwMDAwMDQwLipnY2Njb3JlLip6ZmluYWwtLjAwMDAwMDAxMy4wMDAwMDAwMDIuKnpmaW5hbCIsCn0sClsidG9vbHMvbnVtYWN0bCJdID0gewpmbiA9ICIvd29yay9wcm9qZWN0cy9zb2Z0d2FyZV9zZXQvZWFzeWJ1aWxkL2Fpb24vMjAyM2IvZXB5Yy9tb2R1bGVzL2FsbC90b29scy9udW1hY3RsLzIuMC4xNi1HQ0Njb3JlLTEzLjIuMC5sdWEiLApmdWxsTmFtZSA9ICJ0b29scy9udW1hY3RsLzIuMC4xNi1HQ0Nj
_ModuleTable024_ = b3JlLTEzLjIuMCIsCmxvYWRPcmRlciA9IDYsCnByb3BUID0ge30sCnN0YWNrRGVwdGggPSAzLApzdGF0dXMgPSAiYWN0aXZlIiwKdXNlck5hbWUgPSAidG9vbHMvbnVtYWN0bC8yLjAuMTYtR0NDY29yZS0xMy4yLjAiLAp3ViA9ICIwMDAwMDAwMDIuMDAwMDAwMDAwLjAwMDAwMDAxNi4qZ2NjY29yZS4qemZpbmFsLS4wMDAwMDAwMTMuMDAwMDAwMDAyLip6ZmluYWwiLAp9LAp9LAptcGF0aEEgPSB7CiIvaG9tZS91c2Vycy9ma3VzZWsvLmxvY2FsL2Vhc3lidWlsZC9tb2R1bGVzL2FsbCIKLCAiL21udC9haW9uZ3Bmcy91c2Vycy9ma3VzZWsvd29yay9wcm9qZWN0cy9zb2Z0d2FyZV9zZXQvZWFzeWJ1aWxkL2JpbmFyeS8yMDIzYi9tb2R1bGVzL2FsbCIKLCAiL3dvcmsvcHJvamVj
_ModuleTable025_ = dHMvc29mdHdhcmVfc2V0L2Vhc3lidWlsZC9haW9uLzIwMjNiL2VweWMvbW9kdWxlcy9hbGwiCiwgIi9vcHQvYXBwcy9lYXN5YnVpbGQvZW52aXJvbm1lbnQvbW9kdWxlcyIKLCAiL2N2bWZzL3NvZnR3YXJlLmVlc3NpLmlvL2luaXQvbW9kdWxlcyIKLCAiL29wdC9hcHBzL2Vhc3lidWlsZC9zeXN0ZW1zL2Fpb24vcmhlbDgxMC0yMDI1MDQwNS8yMDIzYi9lcHljL21vZHVsZXMvYWxsIiwgIi9vcHQvYXBwcy9lYXN5YnVpbGQvc3lzdGVtcy9iaW5hcnkvcmhlbDgxMC0yMDI1MDQwNS8yMDIzYi9nZW5lcmljL21vZHVsZXMvYWxsIiwKfSwKc3lzdGVtQmFzZU1QQVRIID0gIi9vcHQvYXBwcy9lYXN5YnVpbGQvZW52aXJvbm1lbnQvbW9kdWxlczovY3ZtZnMvc29mdHdhcmUuZWVzc2ku
_ModuleTable026_ = aW8vaW5pdC9tb2R1bGVzIiwKfQo=
_ModuleTable_Sz_ = 26
__LMOD_REF_COUNT_ACLOCAL_PATH = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/share/aclocal:1
__LMOD_REF_COUNT_CMAKE_LIBRARY_PATH = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0/lib64:1
__LMOD_REF_COUNT_CMAKE_PREFIX_PATH = /home/users/fkusek/.local/easybuild/software/EasyBuild/5.0.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/ScaLAPACK/2.2.0-gompi-2023b-fb:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW.MPI/3.3.10-gompi-2023b:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenBLAS/0.3.24-GCC-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCC/1.2.0-GCCcore-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libevent/2.1.12-GCCcore-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenSSL/1.1:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libpciaccess/0.17-GCCcore-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0:1
__LMOD_REF_COUNT_CPATH = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW.MPI/3.3.10-gompi-2023b/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenBLAS/0.3.24-GCC-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCC/1.2.0-GCCcore-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libevent/2.1.12-GCCcore-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenSSL/1.1/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libpciaccess/0.17-GCCcore-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/include/libxml2:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0/include:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0/include:1
__LMOD_REF_COUNT_LD_LIBRARY_PATH = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/ScaLAPACK/2.2.0-gompi-2023b-fb/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW.MPI/3.3.10-gompi-2023b/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenBLAS/0.3.24-GCC-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCC/1.2.0-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libevent/2.1.12-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenSSL/1.1/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libpciaccess/0.17-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0/lib64:1
__LMOD_REF_COUNT_LIBRARY_PATH = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/ScaLAPACK/2.2.0-gompi-2023b-fb/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW.MPI/3.3.10-gompi-2023b/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenBLAS/0.3.24-GCC-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCC/1.2.0-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libevent/2.1.12-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenSSL/1.1/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libpciaccess/0.17-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0/lib:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0/lib:1
__LMOD_REF_COUNT_MANPATH = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/share/man:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/share/man:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/share/man:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/share/man:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/share/man:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/share/man:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/share/man:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/share/man:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/share/man:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0/share/man:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0/share/man:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0/share/man:1;/usr/share/lmod/lmod/share/man:1;:1;/opt/puppetlabs/puppet/share/man:1
__LMOD_REF_COUNT_MODULEPATH = /home/users/fkusek/.local/easybuild/modules/all:1;/mnt/aiongpfs/users/fkusek/work/projects/software_set/easybuild/binary/2023b/modules/all:1;/work/projects/software_set/easybuild/aion/2023b/epyc/modules/all:1;/opt/apps/easybuild/environment/modules:1;/cvmfs/software.eessi.io/init/modules:1;/opt/apps/easybuild/systems/aion/rhel810-20250405/2023b/epyc/modules/all:1;/opt/apps/easybuild/systems/binary/rhel810-20250405/2023b/generic/modules/all:1
__LMOD_REF_COUNT_PATH = /home/users/fkusek/.local/easybuild/software/EasyBuild/5.0.0/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCC/1.2.0-GCCcore-13.2.0/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libevent/2.1.12-GCCcore-13.2.0/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenSSL/1.1/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/sbin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0/bin:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0/bin:1;/home/users/fkusek/.local/bin:1;/home/users/fkusek/bin:1;/usr/local/bin:1;/usr/bin:1;/usr/local/sbin:1;/usr/sbin:1;/opt/puppetlabs/bin:1;/usr/share/lmod/lmod/libexec:1
__LMOD_REF_COUNT_PKG_CONFIG_PATH = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/ScaLAPACK/2.2.0-gompi-2023b-fb/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenBLAS/0.3.24-GCC-13.2.0/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libevent/2.1.12-GCCcore-13.2.0/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenSSL/1.1/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libpciaccess/0.17-GCCcore-13.2.0/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/lib/pkgconfig:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0/lib/pkgconfig:1
__LMOD_REF_COUNT_PYTHONPATH = /home/users/fkusek/.local/easybuild/software/EasyBuild/5.0.0/lib/python3.11/site-packages:1
__LMOD_REF_COUNT_XDG_DATA_DIRS = /work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FFTW/3.3.10-GCC-13.2.0/share:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/FlexiBLAS/3.3.1-GCC-13.2.0/share:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/OpenMPI/4.1.6-GCC-13.2.0/share:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/PMIx/4.2.6-GCCcore-13.2.0/share:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libfabric/1.19.0-GCCcore-13.2.0/share:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/UCX/1.15.0-GCCcore-13.2.0/share:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/hwloc/2.9.2-GCCcore-13.2.0/share:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/libxml2/2.11.5-GCCcore-13.2.0/share:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/XZ/5.4.4-GCCcore-13.2.0/share:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/numactl/2.0.16-GCCcore-13.2.0/share:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/binutils/2.40-GCCcore-13.2.0/share:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/zlib/1.2.13-GCCcore-13.2.0/share:1;/work/projects/software_set/backup/easybuild/aion/2023b/epyc/software/GCCcore/13.2.0/share:1
which_declare = declare -f
```