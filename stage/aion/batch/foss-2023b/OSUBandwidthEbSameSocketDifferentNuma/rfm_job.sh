#!/bin/bash
#SBATCH --job-name="rfm_OSUBandwidthEbSameSocketDifferentNuma"
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_job.out
#SBATCH --error=rfm_job.err
#SBATCH --exclusive
#SBATCH --partition=batch
#SBATCH --qos=normal
#SBATCH --time=0-00:10:00
#SBATCH --sockets-per-node=1
#SBATCH --cores-per-socket=32
#SBATCH --hint=nomultithread
