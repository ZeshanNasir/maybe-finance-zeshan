import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('expenses_sample.csv')
print(df.head())
df['Amount'] = pd.to_numeric(df['Amount'])
by_category = df.groupby('Category')['Amount'].sum().sort_values()

print("\nSpending by Category:")
print(by_category)

by_category.plot(kind='pie', autopct='%1.1f%%', title='Spending Breakdown by Category')
plt.ylabel('')
plt.tight_layout()
plt.savefig('spending_breakdown.png')
plt.show()
