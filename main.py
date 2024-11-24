from run_single_length_tests import run_single_length_tests
from run_multiple_length_tests import run_multiple_length_tests

from Partition_Algorithms.partition_standard import equal_partition
from Partition_Algorithms.partition_memorized_top_down import equal_partition_top_down
from Partition_Algorithms.partition_tabulation_bottom_up import equal_partition_bottom_up
from Partition_Algorithms.partition_bottom_up_optimization import equal_partition_bottom_up_optimized

algorithmOption = 1
testType = 2

match algorithmOption:
    case 1:
        singleLengthResultFile = "single_length_equal_partition"
        multipleLengthResultFile = "multiple_length_equal_partition"
        algorithm = equal_partition
    case 2:
        singleLengthResultFile = "single_length_memorizes_top_down"
        multipleLengthResultFile = "multiple_length_memorizes_top_down"
        algorithm = equal_partition_top_down
    case 3:
        singleLengthResultFile = "single_length_tabulation_bottom_up"
        multipleLengthResultFile ="multiple_length_tabulation_bottom_up"
        algorithm = equal_partition_bottom_up
    case 4:
        singleLengthResultFile = "single_length_bottom_up_optimized"
        multipleLengthResultFile ="multiple_length_bottom_up_optimized"
        algorithm = equal_partition_bottom_up_optimized
    case _: raise ValueError("Invalid algorithm option. Choose a value between 1 and 4.")

if testType == 1:
    arrayLength = 30
    testsQuantity = 100
    run_single_length_tests(algorithm, testsQuantity, arrayLength, singleLengthResultFile)
    print(f"Tests are finished. Results saved in {singleLengthResultFile}.csv")
elif testType == 2:
    arrayLengths = [10, 20, 30, 40, 50]
    testsQuantityPerLength = 100
    run_multiple_length_tests(algorithm, testsQuantityPerLength, arrayLengths, multipleLengthResultFile)
    print(f"Tests are finished. Results saved in {multipleLengthResultFile}.csv")