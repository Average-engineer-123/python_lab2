import numpy as np

X = np.array([
    [10, 100, 5],
    [12, 110, 6],
    [11, 105, 7],
    [13, 500, 6],
    [14, 108, 8],
    [15, 115, 9]
])

# Column-wise mean
mean = np.mean(X, axis=0)

# Column-wise standard deviation
std = np.std(X, axis=0)

# Column-wise median
median = np.median(X, axis=0)

print("Mean:")
print(mean)

print("\nStandard deviation:")
print(std)

print("\nMedian:")
print(median)

# Detect outliers
outlier_mask = np.abs(X - mean) > 2 * std

print("\nOutlier mask:")
print(outlier_mask)

# Replace outliers with column median
X_clean = X.copy()

X_clean[outlier_mask] = np.broadcast_to(
    median,
    X.shape
)[outlier_mask]

print("\nCleaned data:")
print(X_clean)