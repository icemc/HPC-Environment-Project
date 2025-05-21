#!/bin/bash
#SBATCH --job-name="rfm_OSUBandwidthEasyBuildRunTest_9fd1b159"
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
#SBATCH --ntasks-per-socket=1
