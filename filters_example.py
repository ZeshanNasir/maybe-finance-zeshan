import pandas as pd

df = pd.read_csv('expenses_sample.csv', names=['Date','Merchant','Category','Amount','Type','Description'], header=None)
df = df[1:]
df['Date'] = pd.to_datetime(df['Date'])
df['Amount'] = pd.to_numeric(df['Amount'])
# Only groceries (Livsmedel)
print(df[df['Category'].str.lower() == 'livsmedel'])
# Only weekends
print(df[df['Date'].dt.weekday >= 5])
