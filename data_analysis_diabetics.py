import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes.csv')
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
#print(df)

print(df.head(7))

print(df.info())

print(df.describe())

# استبدال القيم الصفريه الي  nan

columns_to_fix = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

for col in columns_to_fix:
    df[col] = df[col].replace(0, np.nan)
    df[col] = df[col].fillna(df[col].mean())

#print(df)    

plt.figure(figsize=(12, 5)),


plt.subplot(1,2,1)
sns.histplot(data=df , x='Age', hue='Outcome' , multiple='stack', kde=True, palette='Set1')
plt.title('Age distribution and diabetes prevalence rate')
plt.xlabel('Age')
plt.ylabel('pation count')


plt.subplot(1,2,2)
sns.scatterplot(data=df, x='BMI', y='Glucose', hue='Outcome', palette='coolwarm', alpha=0.7)
plt.title('Relationship bettween BMI and Glucose')
plt.xlabel('BMI')
plt.ylabel('Glucose')

plt.tight_layout()
plt.show()


plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='Blues', fmt='.2f')
plt.title('correlation matrix between medical variables')
plt.show()