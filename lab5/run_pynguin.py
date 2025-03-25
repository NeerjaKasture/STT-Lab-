import os
import subprocess

low_cov_files = "low_coverage_files.txt" 
output_dir = "test_suite_B"                
log_dir = os.path.join(output_dir, "logs")

with open(low_cov_files, "r") as f:
    low_coverage_files = [line.split(":")[0].strip() for line in f]

def run_with_timeout(cmd, log_file, timeout=30): # 30 sec timeout per module
    with open(log_file, "w") as log:
        process = subprocess.Popen(cmd, stdout=log, stderr=log)
        try:
            process.wait(timeout=timeout)
            return process.returncode
        except subprocess.TimeoutExpired:
            process.kill()
            log.write("\nTimeout expired for command: " + " ".join(cmd) + "\n")
            return -1
        
for file in low_coverage_files:
    module_name = file.replace("/", ".").replace(".py", "")
    
    log_file = os.path.join(log_dir, f"{module_name}.log")
    
    cmd = ["pynguin", "--project-path", ".", "--module-name", module_name, "--output-path", output_dir]

    print(f"Running: {' '.join(cmd)}")
    return_code = run_with_timeout(cmd, log_file)
    if return_code == 0:
        print(f"Successfully generated tests for {module_name}")
    else:
        print(f"Pynguin failed or timed out for {module_name}. Check logs at {log_file}")
