import pandas as pd
import numpy as np
import time
import os

# Function to execute the tests
def run_single_length_tests(algorithm, tests_quantity, array_length, output_file):
    output_dir = "Tests/Single_Length_Tests"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_file)

    results = []

    # Execute a specified number of tests
    for test_num in range(1, tests_quantity + 1):
        # Generate random array
        array = np.random.randint(1, 100, size=array_length)

        # Capture algorithm's execution time
        start_time = time.perf_counter()
        result = algorithm(array)
        end_time = time.perf_counter()
        elapsed_time = round(end_time - start_time, 10)

        test_result = {
            "Array size": len(array),
            "Result": result,
            "Execution time (s)": elapsed_time
        }
        results.append(test_result)

    # Save test results in a CSV
    df = pd.DataFrame(results)
    df["Execution time (s)"] = df["Execution time (s)"].map(lambda x: f"{x:.10f}")
    df.to_csv(output_path, index=False)