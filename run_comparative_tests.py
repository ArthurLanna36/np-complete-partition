import pandas as pd
import numpy as np
import time
import os

# Function to execute a combined test for multiple algorithms on the same input
def run_comparative_tests(algorithms, tests_quantity, array_length, output_file):
    # Define the directory for saving results
    output_directory = "Tests/Combined_Tests"
    os.makedirs(output_directory, exist_ok=True)
    output_path = os.path.join(output_directory, output_file)

    results = []

    # Execute the specified number of tests
    for test_num in range(1, tests_quantity + 1):
        # Generate a random array
        array = np.random.randint(1, 100, size=array_length)

        # Iterate through each algorithm to test them on the same input
        test_result = {"Test number": test_num, "Array size": array_length}

        for algorithm_name, algorithm in algorithms.items():
            # Measure the execution time of the algorithm
            start_time = time.perf_counter()
            result = algorithm(array)
            end_time = time.perf_counter()
            elapsed_time = round(end_time - start_time, 10)

            # Save the result and execution time for this algorithm
            test_result[f"{algorithm_name} result"] = result
            test_result[f"{algorithm_name} execution time (s)"] = elapsed_time

        results.append(test_result)

    # Save the results to a CSV file
    df = pd.DataFrame(results)

    # Format execution times to ensure uniform decimal places
    for algorithm_name in algorithms.keys():
        column_name = f"{algorithm_name} execution time (s)"
        df[column_name] = df[column_name].map(lambda x: f"{x:.10f}")

    df.to_csv(output_path, index=False)
