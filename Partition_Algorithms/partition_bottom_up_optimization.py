# Python program to partition a Set
# into Two Subsets of Equal Sum

def equal_partition_bottom_up_optimized(array):
    # Calculate sum of the elements in array
    array_sum = sum(array)

    # If sum is odd, there cannot be two
    # subsets with equal sum
    if array_sum % 2 != 0:
        return False

    array_sum = array_sum // 2

    array_size = len(array)
    previous_row = [False] * (array_sum + 1)
    current_row = [False] * (array_sum + 1)

    # Mark previous_row[0] = true as it is true
    # to make sum = 0 using 0 elements
    previous_row[0] = True

    # Fill the subset table in
    # bottom-up manner
    for i in range(1, array_size + 1):
        for j in range(array_sum + 1):
            if j < array[i - 1]:
                current_row[j] = previous_row[j]
            else:
                current_row[j] = (previous_row[j] or previous_row[j - array[i - 1]])

        previous_row = current_row.copy()

    return previous_row[array_sum]