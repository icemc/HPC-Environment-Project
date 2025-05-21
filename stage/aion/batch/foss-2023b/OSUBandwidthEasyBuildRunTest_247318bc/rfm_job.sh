#!/bin/bash
#SBATCH --job-name="rfm_OSUBandwidthEasyBuildRunTest_247318bc"
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_job.out
#SBATCH --error=rfm_job.err
#SBATCH --time=0:5:0
#SBATCH --partition=batch
#SBATCH --qos=normal
#SBATCH --time=0-00:10:00
#SBATCH --exclusive
#SBATCH --sockets-per-node=1
#SBATCH --cores-per-socket=32
#SBATCH --hint=nomultithread
