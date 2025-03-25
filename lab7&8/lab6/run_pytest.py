from collections import defaultdict
import time 
import subprocess

RUNS = 10

test_failures = {}

print(" Running full test suite sequentially 10 times...\n")


for i in range(RUNS):
    print(f" Running test iteration {i+1}/{RUNS}...")
    result = subprocess.run(["pytest","tests", "--tb=short"], capture_output=True, text=True)


    for line in result.stdout.split("\n"):
        if "FAILED" in line and "::" in line:
            test_name = line.split(" ")[1].strip()  
            if test_name not in test_failures:
                test_failures[test_name] = 0
            test_failures[test_name] += 1  
           


failing_tests = {test for test, count in test_failures.items() if count==  RUNS}
flaky_tests = {test for test, count in test_failures.items() if 0 < count < RUNS}


print(f" Failing Tests : {failing_tests}")
print(f" Flaky Tests : {flaky_tests}")


if failing_tests or flaky_tests:
    print("\n Removing failing & flaky tests and creating a clean test suite...")


    exclude_tests = [f"--deselect={test}" for test in failing_tests]
    print(f" Excluding tests: {exclude_tests}")
    cleaned_execution_times = []
    for i in range(1):
        print(f"\n Running cleaned test suite iteration {i+1}/3...")
        start_time = time.time()
        subprocess.run(["pytest", "tests"] + exclude_tests, check=True)
        end_time = time.time()
        cleaned_execution_times.append(end_time - start_time)


    Tseq = sum(cleaned_execution_times) / len(cleaned_execution_times)
    print(f"\n Average execution time after flaky test removal (Tseq): {Tseq:.2f} seconds")


else:
    print("\nNo flaky or failing tests found. Proceeding with performance measurement...")


    execution_times = []
    for i in range(3):
        print(f"\ Running test suite iteration {i+1}/3...")
        start_time = time.time()
        subprocess.run(["pytest","tests"], check=True)
        end_time = time.time()
        execution_times.append(end_time - start_time)


    Tseq = sum(execution_times) / len(execution_times)
    print(f"\n Average execution time (Tseq): {Tseq:.2f} seconds")
