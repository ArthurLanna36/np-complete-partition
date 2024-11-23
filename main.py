import numpy as np

from Partition_Algorithms.partition_standard import equal_partition
from Partition_Algorithms.partition_memorized_top_down import equal_partition_top_down
from Partition_Algorithms.partition_tabulation_bottom_up import equal_partition_bottom_up
from Partition_Algorithms.partition_bottom_up_optimization import equal_partition_bottom_up_optimized

array = np.random.randint(1, 20, size=50)
print(array)

algorithmOption = 1

match algorithmOption:
    case 1:
        executionResult = equal_partition(array)
    case 2:
        executionResult = equal_partition_top_down(array)
    case 3:
        executionResult = equal_partition_bottom_up(array)
    case 4:
        executionResult = equal_partition_bottom_up_optimized(array)
    case _: raise Exception()

if executionResult:
    print("True")
else:
    print("False")