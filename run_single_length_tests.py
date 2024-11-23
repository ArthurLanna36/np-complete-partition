import numpy as np
import pandas as pd
import time

from Partition_Algorithms.partition_standard import equal_partition
from Partition_Algorithms.partition_memorized_top_down import equal_partition_top_down
from Partition_Algorithms.partition_tabulation_bottom_up import equal_partition_bottom_up
from Partition_Algorithms.partition_bottom_up_optimization import equal_partition_bottom_up_optimized

# Function to execute the tests
def run_single_length_tests(algorithm_option, tests_quantity, array_length, output_file):
    # Select the algorithm that will be run
    match algorithm_option:
        case 1:
            algorithm = equal_partition
        case 2:
            algorithm = equal_partition_top_down
        case 3:
            algorithm = equal_partition_bottom_up
        case 4:
            algorithm = equal_partition_bottom_up_optimized
        case _:
            raise ValueError("Invalid algorithm. Choose a value between 1 and 4")

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
    df.to_csv(f"{output_file}.csv", index=False)