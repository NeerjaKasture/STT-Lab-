import matplotlib.pyplot as plt
import numpy as np

baseline_time = 4.56  # from n=1,threads=1,dist=load

configs = [
    "n=1,threads=1,dist=load",
    "n=1,threads=1,dist=no",
    "n=1,threads=auto,dist=load",
    "n=1,threads=auto,dist=no",
    "n=auto,threads=1,dist=load",
    "n=auto,threads=1,dist=no",
    "n=auto,threads=auto,dist=load",
    "n=auto,threads=auto,dist=no",
]

execution_times = [4.56, 4.58, 48.95, 48.78, 4.62, 4.72, 39.37, 39.25]

speedups = [baseline_time / time for time in execution_times]


plt.figure(figsize=(10, 6))
plt.barh(configs, speedups, color="skyblue")
plt.xlabel("Speedup (Relative to Sequential Execution)")
plt.ylabel("Parallelization Configurations")
plt.title("Speedup Comparison of Parallelization Configurations")
plt.gca().invert_yaxis()  

for i, v in enumerate(speedups):
    plt.text(v + 0.05, i, f"{v:.2f}", va='center', fontsize=10)

plt.show()
