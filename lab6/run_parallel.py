import subprocess
import time
import itertools
import json

import multiprocessing

def get_worker_count(n):
    """Returns actual worker count based on pytest -n value."""
    if n == "auto":
        return multiprocessing.cpu_count()  # Auto selects based on CPU cores
    return int(n)

def run_tests(n, threads, dist, repetitions=3):

    failing_tests = {'tests/test_unix.py::TestUnixPath::test_simplify_path', 'tests/test_array.py::TestSummaryRanges::test_summarize_ranges', 'tests/test_unix.py::TestUnixPath::test_full_path', 'tests/test_array.py::TestRemoveDuplicate::test_remove_duplicates'}
    exclude_tests = [f"--deselect={test}" for test in failing_tests]
    worker_count = get_worker_count(n)  # Get actual workers
    results = []
    test_failures = {}    
    for i in range(repetitions):
        cmd = ["pytest","tests", f"-n={n}", f"--dist={dist}", f"--parallel-threads={threads}"]
        start_time = time.time()
        process = subprocess.run(cmd+exclude_tests, capture_output=True, text=True)
        end_time = time.time()
        
        execution_time = end_time - start_time
        failed_tests = []
        
        for line in process.stdout.split("\n"):
            if "FAILED" in line and "::" in line:
                test_name = line.split(" ")[1].strip()
                failed_tests.append(test_name)
                if test_name not in test_failures:
                    test_failures[test_name] = 0
                test_failures[test_name] += 1  
                
        results.append({
            "execution_time": execution_time,
            "failed_tests": failed_tests,
        })
    
    avg_time = sum(res["execution_time"] for res in results) / repetitions
    unique_failed_tests = list(test_failures.keys())
    
    return {
        "n": n,
        "worker_count": worker_count,  # Store actual workers used
        "threads": threads,
        "dist": dist,
        "average_time": avg_time,
        "flaky_tests": unique_failed_tests,
        "failures_per_run": results,
        "test_failure_counts": dict(test_failures)
    }

if __name__ == "__main__":
    n_values = ["1", "auto"]
    threads_values = ["1", "auto"]
    dist_values = ["load", "no"]
    
    all_results = []
    
    for n, threads, dist in itertools.product(n_values, threads_values, dist_values):
        print(f"Running tests with -n={n}, --parallel-threads={threads}, --dist={dist}")
        result = run_tests(n, threads, dist)
        all_results.append(result)
    
    with open("test_results.json", "w") as f:
        json.dump(all_results, f, indent=4)
    
    print("Test execution completed. Results saved to test_results.json")
