import pandas as pd
import matplotlib.pyplot as plt
import os

csv_path = os.path.join(os.path.dirname(__file__), 'alert_data.csv')

df = pd.read_csv(csv_path)
df['severity'].value_counts().sort_index().plot(kind='bar')
plt.title("Alert Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
