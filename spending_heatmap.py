import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('expenses_sample.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Amount'] = pd.to_numeric(df['Amount'])
df['DayOfWeek'] = df['Date'].dt.day_name()

heatmap_data = df.groupby('DayOfWeek')['Amount'].sum().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

print("\nSpending by Day of Week:")
print(heatmap_data)

plt.figure(figsize=(8, 2))
sns.heatmap(heatmap_data.values.reshape(1,7), annot=True, fmt=".0f", cmap="YlGnBu", yticklabels=False)
plt.title('Spending by Day of Week')
plt.xticks(ticks=range(7), labels=heatmap_data.index)
plt.yticks([])
plt.show()
