import pandas as pd
import numpy as np
import time
import os

# Function to execute the tests for multiple array lengths
def run_multiple_length_tests(algorithm, tests_quantity_per_length, array_lengths, output_file):
    output_directory = 'Tests/Multiple_Length_Tests'
    os.makedirs(output_directory, exist_ok=True)
    output_path = os.path.join(output_directory, output_file)
    results = []

    # Iterate over the specified array lengths
    for array_length in array_lengths:
        # Execute a specified number of tests for each array length
        for test_num in range(1, tests_quantity_per_length + 1):
            # Generate random array
            array = np.random.randint(1, 100, size=array_length)

            # Capture algorithm's execution time
            start_time = time.perf_counter()
            result = algorithm(array)
            end_time = time.perf_counter()
            elapsed_time = round(end_time - start_time, 10)

            # Save test result
            test_result = {
                "Test number": test_num,
                "Array size": len(array),
                "Result": result,
                "Execution time (s)": elapsed_time
            }
            results.append(test_result)

    # Save all test results in a CSV
    df = pd.DataFrame(results)
    df["Execution time (s)"] = df["Execution time (s)"].map(lambda x: f"{x:.10f}")
    df.to_csv(output_path, index=False)
