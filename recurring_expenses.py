import pandas as pd

df = pd.read_csv('expenses_sample.csv', names=['Date','Merchant','Category','Amount','Type','Description'], header=None)
df = df[1:]
df['Amount'] = pd.to_numeric(df['Amount'])
recurring = df['Merchant'][df['Description'].str.contains('abonnemang|månads', case=False, na=False)]
print("Potential recurring/subscription merchants:")
print(recurring.value_counts())
