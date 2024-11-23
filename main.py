import numpy as np

from run_single_length_tests import run_single_length_tests

algorithmOption = 1
testsQuantity = 100
arrayLength = 30

match algorithmOption:
    case 1:
        outputFileName = "equal_partition_results"
    case 2:
        outputFileName = "memorizes_top_down_results"
    case 3:
        outputFileName = "tabulation_bottom_up_results"
    case 4:
        outputFileName = "bottom_up_optimized_results"
    case _: raise ValueError("Invalid algorithm option. Choose a value between 1 and 4.")

run_single_length_tests(algorithmOption, testsQuantity, arrayLength, outputFileName)
print(f"Tests are finished. Results saved in {outputFileName}.csv")