import pandas as pd
import matplotlib.pyplot as plt

# Load expense data
df = pd.read_csv('expenses_sample.csv')

# Group by Category
summary = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
print("Expense by category:")
print(summary)

# Plot
summary.plot(kind='pie', autopct='%1.1f%%', title='Spending Breakdown by Category')
plt.ylabel('')
plt.tight_layout()
plt.savefig('spending_breakdown.png')
plt.show()
