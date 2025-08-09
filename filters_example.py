import pandas as pd

df = pd.read_csv('expenses_sample.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Amount'] = pd.to_numeric(df['Amount'])

# Only “Essentials”
print("\nEssentials Expenses:")
print(df[df['Category'] == 'Essentials'])

# Only weekends
print("\nWeekend Expenses:")
print(df[df['Date'].dt.dayofweek >= 5])
