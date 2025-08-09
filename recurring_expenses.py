import pandas as pd

df = pd.read_csv('expenses_sample.csv')
merchant_counts = df['Merchant'].value_counts()
print("\nMost Frequent Merchants (possible subscriptions):")
print(merchant_counts)
