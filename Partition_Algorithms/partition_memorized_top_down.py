# Python program to partition a Set
# into Two Subsets of Equal Sum

def is_subset_sum(array_size, array, new_sum, memory):
    # base cases
    if new_sum == 0:
        return True
    if array_size == 0:
        return False

    if memory[array_size - 1][new_sum] != -1:
        return memory[array_size - 1][new_sum]

    # If element is greater than sum, then ignore it
    if array[array_size - 1] > new_sum:
        return is_subset_sum(array_size - 1, array, new_sum, memory)

    # Check if sum can be obtained by any of the following
    # (a) including the current element
    # (b) excluding the current element
    memory[array_size - 1][new_sum] = is_subset_sum(array_size - 1, array, new_sum, memory) or \
                                      is_subset_sum(array_size - 1, array, new_sum - array[array_size - 1], memory)
    return memory[array_size - 1][new_sum]

def equal_partition_top_down(array):
    # Calculate sum of the elements in array
    array_sum = sum(array)

    # If sum is odd, there cannot be two
    # subsets with equal sum
    if array_sum % 2 != 0:
        return False

    memo = [[-1 for _ in range(array_sum + 1)] for _ in range(len(array))]

    # Find if there is subset with sum equal
    # to half of total sum
    return is_subset_sum(len(array), array, array_sum // 2, memo)