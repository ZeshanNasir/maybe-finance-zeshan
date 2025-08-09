import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('expenses_sample.csv', names=['Date','Merchant','Category','Amount','Type','Description'], header=None)
df = df[1:]  # Skip header if already present as data
df['Amount'] = pd.to_numeric(df['Amount'])
expenses = df[df['Amount'] < 0]

by_category = expenses.groupby('Category')['Amount'].sum().abs().sort_values()
by_category.plot(kind='pie', autopct='%1.1f%%', title='Spending Breakdown by Category')
plt.ylabel('')
plt.tight_layout()
plt.savefig('spending_breakdown.png')
plt.show()
