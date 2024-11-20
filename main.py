import numpy as np

from Partition_Algorithms.partition_standard import equal_partition
from Partition_Algorithms.partition_tabulation_bottom_up import equal_partition_bottom_up

array = np.random.randint(1, 20, size=50)
print(array)

# if equal_partition(array):
#     print("True")
# else:
#     print("False")

if equal_partition_bottom_up(array):
    print("True")
else:
    print("False")