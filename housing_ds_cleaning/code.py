import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Housing.csv")

# -----------------------------
# 1. Basic information
# -----------------------------

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())

print("\nStatistical summary:")
print(df.describe())


# -----------------------------
# 2. Missing values
# -----------------------------

print("\nMissing values:")
print(df.isnull().sum())


# -----------------------------
# 3. Duplicate values
# -----------------------------

print("\nNumber of duplicates:")
print(df.duplicated().sum())

df = df.drop_duplicates()


# -----------------------------
# 4. Numerical columns
# -----------------------------

numeric_cols = df.select_dtypes(
    include=np.number
).columns

print("\nNumerical columns:")
print(numeric_cols)


# -----------------------------
# 5. Fill missing numerical values
# -----------------------------

for col in numeric_cols:
    df[col] = df[col].fillna(
        df[col].median()
    )


# -----------------------------
# 6. Categorical columns
# -----------------------------

categorical_cols = df.select_dtypes(
    include='object'
).columns

for col in categorical_cols:
    df[col] = df[col].fillna(
        df[col].mode()[0]
    )


# -----------------------------
# 7. Histograms
# -----------------------------

df[numeric_cols].hist(figsize=(12, 8))

plt.tight_layout()
plt.show()


# -----------------------------
# 8. Correlation heatmap
# -----------------------------

plt.figure(figsize=(10, 7))

sns.heatmap(
    df[numeric_cols].corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")
plt.show()


# -----------------------------
# 9. Box plots
# -----------------------------

for col in numeric_cols:

    plt.figure(figsize=(7, 4))

    sns.boxplot(
        x=df[col]
    )

    plt.title(f"Boxplot of {col}")
    plt.show()


# -----------------------------
# 10. Pairplot
# -----------------------------

sns.pairplot(
    df[numeric_cols]
)

plt.show()