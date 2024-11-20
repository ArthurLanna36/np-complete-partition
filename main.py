import numpy as np

from Partition_Algorithms.partition_standard import equal_partition

array = np.random.randint(1, 20, size=10)
print(array)

if equal_partition(array):
    print("True")
else:
    print("False")