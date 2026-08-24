import pandas as pd

df = pd.DataFrame({
    'ID': [101,102,103,101,104,102,105],
    'Name': ['A','B','C','A','D','B','E'],
    'Age': [20,21,22,20,23,21,24],
    'Score': [80,75,90,85,88,75,92]
})

# 1. Identify duplicated IDs
duplicated_ids = df[
    df['ID'].duplicated(keep=False)
]

print("Duplicated IDs:")
print(duplicated_ids)


# 2. Check whether records are identical
duplicate_groups = df.groupby('ID').filter(
    lambda x: len(x) > 1
)

print("\nRecords having duplicate IDs:")
print(duplicate_groups)


# Check identical records within each ID
for id_value, group in df.groupby('ID'):
    if len(group) > 1:
        identical = group.drop(columns=['Score']).nunique().max() == 1
        print(f"ID {id_value} records identical: {identical}")


# 3. Keep record having highest Score
clean_df = (
    df.sort_values('Score', ascending=False)
      .drop_duplicates('ID', keep='first')
      .sort_values('ID')
      .reset_index(drop=True)
)

print("\nClean DataFrame:")
print(clean_df)


# 5. Number of records removed
removed = len(df) - len(clean_df)

print("\nRecords removed:", removed)