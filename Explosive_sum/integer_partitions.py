import numpy as np

def partitions(n):
    partition_matrix = np.zeros((n+1, n+1))
    partition_matrix[:, 0] = 1
    for col in range(1, n+1):
        for row in range(1, n+1):
            if col == 1:
                partition_matrix[row, col] = 1
            if row == 1:
                partition_matrix[row, col] = 1
            else:
                sum_without_last_summand = partition_matrix[row-1, col]
                sum_with_last_summand = partition_matrix[row, col - row]
                partition_matrix[row, col] = sum_without_last_summand + \
                                             sum_with_last_summand
    return int(partition_matrix[n, n])
n = int(input())
print(partitions(n))
