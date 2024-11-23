# Python program to partition a Set
# into Two Subsets of Equal Sum

def equal_partition_bottom_up(array):
    # Calculate sum of the elements in array
    array_sum = sum(array)
    array_size = len(array)

    # If sum is odd, there cannot be two
    # subsets with equal sum
    if array_sum % 2 != 0:
        return False

    array_sum = array_sum // 2

    # Create a 2D array for storing results
    # of subproblems
    table = [[False] * (array_sum + 1) for _ in range(array_size + 1)]

    # If sum is 0, then answer is true (empty subset)
    for i in range(array_size + 1):
        table[i][0] = True

    # Fill the table in bottom-up manner
    for i in range(1, array_size + 1):
        for j in range(1, array_sum + 1):
            if j < array[i - 1]:
                # Exclude the current element
                table[i][j] = table[i - 1][j]
            else:
                # Include or exclude
                table[i][j] = table[i - 1][j] or table[i - 1][j - array[i - 1]]

    return table[array_size][array_sum]