# dashboard.py
        import pandas as pd
        import matplotlib.pyplot as plt

        df = pd.read_csv("visualization/alert_data.csv")
        df['severity'].value_counts().plot(kind='bar')
        plt.title("Alert Severity Distribution")
        plt.xlabel("Severity")
        plt.ylabel("Count")
        plt.show()