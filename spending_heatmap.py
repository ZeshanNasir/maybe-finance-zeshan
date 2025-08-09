import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('expenses_sample.csv', names=['Date','Merchant','Category','Amount','Type','Description'], header=None)
df = df[1:]
df['Date'] = pd.to_datetime(df['Date'])
df['Amount'] = pd.to_numeric(df['Amount'])
expenses = df[df['Amount'] < 0]
expenses['DayOfWeek'] = expenses['Date'].dt.day_name()

heatmap_data = expenses.groupby('DayOfWeek')['Amount'].sum().reindex(
    ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
plt.figure(figsize=(8, 2))
sns.heatmap(heatmap_data.values.reshape(1,7), annot=True, fmt=".0f", cmap="YlGnBu", yticklabels=False)
plt.title('Outflow by Day of Week (SEK)')
plt.xticks(ticks=range(7), labels=heatmap_data.index)
plt.yticks([])
plt.show()
