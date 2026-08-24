import numpy as np

P = np.array([
    [1, 2],
    [4, 6],
    [7, 3],
    [2, 8],
    [9, 5]
])

# Broadcasting
difference = P[:, np.newaxis, :] - P[np.newaxis, :, :]

# Euclidean distance
distance_matrix = np.sqrt(
    np.sum(difference ** 2, axis=2)
)

print("Distance Matrix:")
print(distance_matrix)


# Maximum distance
max_index = np.unravel_index(
    np.argmax(distance_matrix),
    distance_matrix.shape
)

i, j = max_index

print("\nMaximum distance:", distance_matrix[i, j])
print("Pair of points:", i + 1, "and", j + 1)