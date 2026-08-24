import numpy as np

A = np.array([
    [12, 5, 8, 20],
    [7, 15, 3, 11],
    [25, 9, 18, 6],
    [10, 14, 2, 16]
])

# Mean of each row
row_means = np.mean(A, axis=1)

print("Row means:")
print(row_means)

# 2, 3, 4. Compare every element with its row mean
binary_matrix = (A > row_means[:, np.newaxis]).astype(int)

print("\nBinary matrix:")
print(binary_matrix)

# 5. Number of elements above row mean
count_above_mean = np.sum(binary_matrix, axis=1)

print("\nNumber of elements above row mean:")
print(count_above_mean)

max_count = np.max(count_above_mean)

rows = np.where(count_above_mean == max_count)[0]

print("\nMaximum number of elements above mean:", max_count)
print("Rows:", rows + 1)