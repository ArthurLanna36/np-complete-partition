def is_subset_sum(array_size, array, new_sum):
    # Base cases
    if new_sum == 0:
        return True
    if array_size == 0:
        return False

    # If element is greater than sum, then ignore it
    if array[array_size - 1] > new_sum:
        return is_subset_sum(array_size - 1, array, new_sum)

    # Check if sum can be obtained by any of the following:
    # (a) including the current element
    # (b) excluding the current element
    return is_subset_sum(array_size - 1, array, new_sum) or \
        is_subset_sum(array_size - 1, array, new_sum - array[array_size - 1])

def equal_partition(array):
    # Calculate sum of the elements in array
    array_sum = sum(array)

    # If sum is odd, there cannot be two
    # subsets with equal sum
    if array_sum % 2 != 0:
        return False

    # Find if there is subset with sum equal
    # to half of total sum
    return is_subset_sum(len(array), array, array_sum // 2)