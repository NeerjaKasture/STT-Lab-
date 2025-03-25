import os
import subprocess
import json
import csv

repositories = ["scrapy"]

SEVERITY_LEVELS = ["HIGH", "MEDIUM", "LOW"]
CONFIDENCE_LEVELS = ["HIGH", "MEDIUM", "LOW"]


def get_last_100_commits(repo_path):

    os.chdir(repo_path)
    commit_list = subprocess.check_output(
        ["git", "log", "--pretty=format:%H", "-n", "100", "--no-merges"],
        text=True
    ).split("\n")

    commit_list.reverse()

    return commit_list

def run_bandit_on_commit(repo_path, commit_hash):
    print(f"Running Bandit on commit {commit_hash} in repo {repo_path}")  # Debug print

    result= subprocess.run(["git", "checkout", commit_hash], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode != 0:
        print(f"Failed to checkout commit {commit_hash}: {result.stderr.strip()}")
        
    bandit_output = subprocess.run(
        ["bandit", "-r", ".", "-f", "json","-o","temp.json"], text=True, check=False
    )

        
def parse_bandit_output():
    
    print("Parsing Bandit output...")
    with open("temp.json") as f:
        bandit_json = json.load(f)
    
    severity_counts = {level: 0 for level in SEVERITY_LEVELS}
    confidence_counts = {level: 0 for level in CONFIDENCE_LEVELS}
    unique_cwes = set()

    for issue in bandit_json["results"]:
        severity = issue.get("issue_severity", "").upper()
        confidence = issue.get("issue_confidence", "").upper()
        cwe = issue.get("issue_cwe", {}).get("id", "")  # Extract CWE ID safely


        if severity in severity_counts:
            severity_counts[severity] += 1

        if confidence in confidence_counts:
            confidence_counts[confidence] += 1

        if cwe:  
            unique_cwes.add(str(cwe)) 
    return severity_counts, confidence_counts, unique_cwes  # Return CWE count


def main():

    results = []

    for repo in repositories:
        print(f"Processing repository: {repo}")
        repo_path = os.path.abspath(repo)  # Get the absolute path of the repo
        commit_hashes = get_last_100_commits(repo_path)

        for commit in commit_hashes:
            print(f"Analyzing commit {commit} in {repo}...")
            run_bandit_on_commit(repo_path, commit)

            severity, confidence, cwes = parse_bandit_output()
            results.append({
                "commit": commit,
                "HIGH_severity": severity["HIGH"],
                "MEDIUM_severity": severity["MEDIUM"],
                "LOW_severity": severity["LOW"],
                "HIGH_confidence": confidence["HIGH"],
                "MEDIUM_confidence": confidence["MEDIUM"],
                "LOW_confidence": confidence["LOW"],
                "CWEs": ','.join(cwes),
                "No. of CWEs": len(cwes)

            })

        print(f"Restoring repository {repo} to the main branch...")
        os.chdir(repo_path)  # Ensure this is the correct path
        subprocess.run(["git", "checkout", "main"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


    with open("bandit_scrapy.csv", "w", newline="") as csvfile:
        fieldnames = [ "commit", "HIGH_severity", "MEDIUM_severity", "LOW_severity",
                      "HIGH_confidence", "MEDIUM_confidence", "LOW_confidence", "CWEs","No. of CWEs"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


    print("Analysis completed. Results saved in bandit_analysis.csv")


if __name__ == "__main__":
    main()


