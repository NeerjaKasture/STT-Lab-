import pandas as pd
import matplotlib.pyplot as plt

csv_file = "bandit_pipenv.csv"
df = pd.read_csv(csv_file)
df["commit_index"] = range(1, len(df) + 1)

fig, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True) 

# High Severity Plot
axes[0].plot(df["commit_index"], df["HIGH_severity"],  color="red", linestyle="-")
axes[0].set_ylabel("High Severity")
axes[0].set_title("High Severity Vulnerabilities Over Commits")
axes[0].grid()

# Medium Severity Plot
axes[1].plot(df["commit_index"], df["MEDIUM_severity"],  color="orange", linestyle="-")
axes[1].set_ylabel("Medium Severity")
axes[1].set_title("Medium Severity Vulnerabilities Over Commits")
axes[1].grid()

# Low Severity Plot
axes[2].plot(df["commit_index"], df["LOW_severity"],  color="blue", linestyle="-")
axes[2].set_ylabel("Low Severity")
axes[2].set_title("Low Severity Vulnerabilities Over Commits")
axes[2].set_xlabel("Commits ")
axes[2].grid()

plt.xticks([])  
plt.tight_layout()
plt.show()
