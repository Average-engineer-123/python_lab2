import pandas as pd

df = pd.DataFrame({
    'Date': [
        '2026-01-01',
        '2026-01-02',
        '2026-01-04',
        '2026-01-05',
        '2026-01-08',
        '2026-01-09'
    ],
    'Sales': [100,120,150,130,180,200]
})

# 1. Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set Date as index
df = df.set_index('Date')

# 2 & 3. Create complete date range
full_dates = pd.date_range(
    start=df.index.min(),
    end=df.index.max(),
    freq='D'
)

df = df.reindex(full_dates)

df.index.name = 'Date'

print("Reindexed DataFrame:")
print(df)


# 5. Calculate 3-day rolling average
df['Rolling_Average'] = df['Sales'].rolling(
    window=3,
    min_periods=1
).mean()

print("\nWith rolling average:")
print(df)


# 6. Date having maximum rolling average
max_date = df['Rolling_Average'].idxmax()

print("\nMaximum rolling average date:")
print(max_date)

print(
    "Maximum rolling average:",
    df.loc[max_date, 'Rolling_Average']
)