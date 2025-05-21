performance_data = {
    "Bandwidth": {
        "inter_node": {
            "From Source": 10019.00,
            "EESSI": 8566.67,
            "EasyBuild": 8600.14,
        },
        "diff_socket_same_node": {
            "From Source": 4932.75,
            "EESSI": 17374.70,
            "EasyBuild": 17410.00,
        },
        "diff_numa_same_socket": {
            "From Source": 4523.73,
            "EESSI": 16892.00,
            "EasyBuild": 17415.30,
        },
        "same_numa": {
            "From Source": 5183.22,
            "EESSI": 4865.29,
            "EasyBuild": 17652.60,
        }
    },
    "Latency": {
        "inter_node": {
            "From Source": 7.20,
            "EESSI": 4.67,
            "EasyBuild": 9.77,
        },
        "diff_socket_same_node": {
            "From Source": 5.67,
            "EESSI": 4.14,
            "EasyBuild": 11.71,
        },
        "diff_numa_same_socket": {
            "From Source": 1.93,
            "EESSI": 1.86,
            "EasyBuild": 1.91,
        },
        "same_numa": {
            "From Source": 2.20,
            "EESSI": 1.88,
            "EasyBuild": 6.75,
        }
    }
}

# Unit information
units = {
    "Bandwidth": "MB/s",
    "Latency": "µs"
}

# Variant descriptions for better axis labels
variant_descriptions = {
    "inter_node": "Inter-node",
    "diff_socket_same_node": "Diff socket, same node",
    "diff_numa_same_socket": "Diff NUMA, same socket",
    "same_numa": "Same NUMA"
}

aion_performance_data = {
    "Bandwidth": {
        "inter_node": {
            "From Source": 12326.6,
            "EESSI": 12328.2,
            "EasyBuild": 12325.1,
        },
        "diff_socket_same_node": {
            "From Source": 13200.1,
            "EESSI": 10937.0,
            "EasyBuild": 13173.1,
        },
        "diff_numa_same_socket": {
            "From Source": 12963.3,
            "EESSI": 14877.9,
            "EasyBuild": 12993.0,
        },
        "same_numa": {
            "From Source": 14953.1,
            "EESSI": 14500.6,
            "EasyBuild": 14685.1,
        }
    },
    "Latency": {
        "inter_node": {
            "From Source": 4.01,
            "EESSI": 4.01,
            "EasyBuild": 4.01,
        },
        "diff_socket_same_node": {
            "From Source": 2.28,
            "EESSI": 2.27,
            "EasyBuild": 2.28,
        },
        "diff_numa_same_socket": {
            "From Source": 2.28,
            "EESSI": 2.28,
            "EasyBuild": 2.28,
        },
        "same_numa": {
            "From Source": 0.55,
            "EESSI": 0.57,
            "EasyBuild": 0.59,
        }
    }
}


import matplotlib.pyplot as plt
import numpy as np

# Define the plotting function for individual systems (unchanged)
def plot_system_performance(system_name, performance_data, save_path=None):
    variants = list(performance_data["Bandwidth"].keys())
    build_methods = ["From Source", "EESSI", "EasyBuild"]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))
    fig.suptitle(f'Performance Metrics - {system_name}', fontsize=16)
    
    # Bandwidth plot
    width = 0.25
    x = np.arange(len(variants))
    
    for i, method in enumerate(build_methods):
        values = [performance_data["Bandwidth"][v].get(method, 0) for v in variants]
        ax1.bar(x + i*width, values, width, label=method)
    
    ax1.set_xticks(x + width)
    ax1.set_xticklabels([variant_descriptions[v] for v in variants], rotation=45)
    ax1.set_ylabel(f"Bandwidth ({units['Bandwidth']})")
    ax1.set_title("Bandwidth Performance")
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.6)
    
    # Latency plot
    for i, method in enumerate(build_methods):
        values = [performance_data["Latency"][v].get(method, 0) for v in variants if v in performance_data["Latency"]]
        ax2.bar(x[:len(values)] + i*width, values, width, label=method)
    
    ax2.set_xticks(x[:len(values)] + width)
    ax2.set_xticklabels([variant_descriptions[v] for v in variants if v in performance_data["Latency"]], rotation=45)
    ax2.set_ylabel(f"Latency ({units['Latency']})")
    ax2.set_title("Latency Performance")
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()

# New separate comparison plotting functions
def plot_bandwidth_comparison(iris_data, aion_data, save_path=None):
    variants = list(iris_data["Bandwidth"].keys())
    build_methods = ["From Source", "EESSI", "EasyBuild"]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    width = 0.35
    x = np.arange(len(variants))
    
    for i, method in enumerate(build_methods):
        iris_values = [iris_data["Bandwidth"][v].get(method, 0) for v in variants]
        aion_values = [aion_data["Bandwidth"][v].get(method, 0) for v in variants]
        
        ax.bar(x + i*width*2, iris_values, width, label=f'Iris {method}', color=f'C{i}', alpha=0.7)
        ax.bar(x + i*width*2 + width, aion_values, width, label=f'Aion {method}', color=f'C{i}', hatch='//', alpha=0.7)
    
    ax.set_xticks(x + width*len(build_methods))
    ax.set_xticklabels([variant_descriptions[v] for v in variants], rotation=45)
    ax.set_ylabel(f"Bandwidth ({units['Bandwidth']})")
    ax.set_title("Bandwidth Comparison: Iris vs Aion")
    ax.legend(ncol=2)
    ax.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()

def plot_latency_comparison(iris_data, aion_data, save_path=None):
    variants = [v for v in iris_data["Bandwidth"].keys() if v in iris_data["Latency"]]
    build_methods = ["From Source", "EESSI", "EasyBuild"]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    width = 0.35
    x = np.arange(len(variants))
    
    for i, method in enumerate(build_methods):
        iris_values = [iris_data["Latency"][v].get(method, 0) for v in variants]
        aion_values = [aion_data["Latency"][v].get(method, 0) for v in variants]
        
        ax.bar(x + i*width*2, iris_values, width, label=f'Iris {method}', color=f'C{i}', alpha=0.7)
        ax.bar(x + i*width*2 + width, aion_values, width, label=f'Aion {method}', color=f'C{i}', hatch='//', alpha=0.7)
    
    ax.set_xticks(x + width*len(build_methods))
    ax.set_xticklabels([variant_descriptions[v] for v in variants], rotation=45)
    ax.set_ylabel(f"Latency ({units['Latency']})")
    ax.set_title("Latency Comparison: Iris vs Aion")
    ax.legend(ncol=2)
    ax.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()

# Generate and save all plots
plot_system_performance("Iris", performance_data, "iris_performance.png")
plot_system_performance("Aion", aion_performance_data, "aion_performance.png")
plot_bandwidth_comparison(performance_data, aion_performance_data, "bandwidth_comparison.png")
plot_latency_comparison(performance_data, aion_performance_data, "latency_comparison.png")

print("Plots generated and saved as:")
print("- iris_performance.png")
print("- aion_performance.png")
print("- bandwidth_comparison.png")
print("- latency_comparison.png")