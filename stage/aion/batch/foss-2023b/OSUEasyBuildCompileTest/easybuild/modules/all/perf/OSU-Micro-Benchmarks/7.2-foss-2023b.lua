help([==[

Description
===========
OSU Micro-Benchmarks


More information
================
 - Homepage: https://mvapich.cse.ohio-state.edu/benchmarks/
]==])

whatis([==[Description: OSU Micro-Benchmarks]==])
whatis([==[Homepage: https://mvapich.cse.ohio-state.edu/benchmarks/]==])
whatis([==[URL: https://mvapich.cse.ohio-state.edu/benchmarks/]==])

local root = "/mnt/aiongpfs/users/fkusek/HPC-Environment-Project/stage/aion/batch/foss-2023b/OSUEasyBuildCompileTest/easybuild/software/OSU-Micro-Benchmarks/7.2-foss-2023b"

conflict("perf/OSU-Micro-Benchmarks")

depends_on("toolchain/foss/2023b")

prepend_path("CMAKE_PREFIX_PATH", root)
prepend_path("PATH", pathJoin(root, "libexec/osu-micro-benchmarks/mpi/collective"))
prepend_path("PATH", pathJoin(root, "libexec/osu-micro-benchmarks/mpi/one-sided"))
prepend_path("PATH", pathJoin(root, "libexec/osu-micro-benchmarks/mpi/pt2pt"))
prepend_path("PATH", pathJoin(root, "libexec/osu-micro-benchmarks/mpi/startup"))
setenv("EBROOTOSUMINMICROMINBENCHMARKS", root)
setenv("EBVERSIONOSUMINMICROMINBENCHMARKS", "7.2")
setenv("EBDEVELOSUMINMICROMINBENCHMARKS", pathJoin(root, "easybuild/perf-OSU-Micro-Benchmarks-7.2-foss-2023b-easybuild-devel"))

-- Built with EasyBuild version 5.0.0-rd4904b19ad7c067333f8c7679b1b1f1a0512abde
