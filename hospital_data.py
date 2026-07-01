import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('hospital_data.csv')
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)


print(df.head(7))

print(df.info())

df['Admission_Date'] = pd.to_datetime(df['Admission_Date'])

print(df.dtypes)

print(df['Diagnosis'].value_counts())

print(df.groupby('Admission_Date')['Age'].mean())

plt.figure(figsize=(10, 6))
sns.countplot(data=df , x='Admission_Date', palette='pastel')
plt.title('Hospital Admission Diagnostics Distribution ')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('hosopital_chart.png')
plt.show()




