## HPC Cluster Regression Testing Framework

### Overview
--------
This repository contains a comprehensive regression testing framework for HPC clusters using ReFrame. It validates performance across different software deployment methods (EESSI, EasyBuild, and source builds) using the OSU Micro-Benchmarks as a test suite.

### Repository Structure
--------------------

```text
root/
├── README.md                 # This documentation
├── project_description.md    # Detailed project background
├── reframe/
│   ├── easybuild/            # EasyBuild deployment test cases
│   ├── eessi/                # EESSI deployment test cases
│   ├── source/               # Source build test cases
│   └── configs/
│       └── configs.py        # ReFrame configuration files
└── analysis/                 # Sample Performance analysis tools
    ├── plot_generation.py    # Visualization scripts
    ├── iris_performance.png  # Sample output
    └── aion_performance.png  # Sample output
```

### Key Features
------------
- Multi-Deployment Validation: Tests three deployment methodologies:
  * Source compilation
  * EasyBuild installations
  * EESSI software stack

- Performance Benchmarking: Measures:
  * Latency (µs) across different node configurations
  * Bandwidth (MB/s) for various communication patterns

- Sample Reporting: Generates visual performance comparisons between:
  * Different deployment methods
  * Different HPC systems (Iris vs Aion)

### Getting Started
---------------
Prerequisites:
- Access to ULHPC cluster (Iris or Aion)
- ReFrame 4.7.4 or later

Accessing the HPC cluster
1. For Iris (You will need access) 
    ``` 
    ssh iris-cluster
    salloc -p interactive --qos debug --time=2:00:00 -N 1 -n 1 -c 1
    ```
2. For Aion (You will need access) 
    ``` 
    ssh aion-cluster
    salloc -p interactive --qos debug --time=2:00:00 -N 1 -n 1 -c 1
    ```
Installation:
1. Clone the repository:
   ```
   git clone git@github.com:icemc/HPC-Environment-Project.git
   cd HPC-Environment-Project
   ```

2. Set up environment:
   ```
   module load devel/ReFrame/4.7.4-GCCcore-13.2.0
   ```

### Running Tests
------------
On Iris or Aion Cluster

#### For source builds:
```
reframe -C reframe/configs/configs.py -c reframe/source -r --performance-report
```

#### For EasyBuild:
```
reframe -C reframe/configs/configs.py -c reframe/easybuild -r --performance-report
```
#### For EESSI:
```
reframe -C reframe/configs/configs.py -c reframe/eessi -r --performance-report
```
### Sample Performance reports

#### 1. Aion Performance 

![Aion performance](./analysis/aion_performance.png)

#### 2. Iris Performance 

![Aion performance](./analysis/iris_performance.png)

### Resources
-------------
- ReFrame Testing Framework: https://reframe-hpc.readthedocs.io
- EESSI Software Stack: https://www.eessi.io/docs
- OSU Micro-Benchmarks: http://mvapich.cse.ohio-state.edu/benchmarks/
- ULHPC User Guide: https://hpc.uni.lu/users/docs/


### License
-------
MIT License