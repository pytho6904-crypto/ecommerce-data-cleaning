import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#قراءت الملف
df = pd.read_csv('all_data.csv',encoding='iso-8859-1')
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)


#استكشاف الملف قبل التنظيف
print(df.shape)
print(df.head(5))

missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

#مرحله التنظيف

duplicate_count = df.duplicated().sum()

if duplicate_count > 0:
    df.drop_duplicates(inplace=True)
    print("succssfully to {duplicate_count} ")

if 'UnitPrice' in df.columns:
    df['UnitPrice'] = df['UnitPrice'].fillna(df['UnitPrice'].mean())
    print("succssfully, to change from na to unna by mean ")

if 'OrderDate' in df.columns:
    df['OrderDate'] = pd.to_datetime(df['OrderDate'],errors='coerce')



#    التحليل البصري بالرسومات البيانيه  الاعلي 5 منتجات       
if 'TotalAmount' in df.columns and 'ProductID' in df.columns:
    plt.figure(figsize=(10, 6))
    top_product = df.groupby('ProductID')['TotalAmount'].sum().nlargest((5))

    sns.barplot(x=top_product.values, y=top_product.index, palette='viridis')
    plt.title('Top 5 Best- selling Products', fontsize=14, fontweight='bold')
    plt.xlabel('Total Quantity sold',fontsize=12)
    plt.ylabel('product Name', fontsize=12)

# حفظ الرسومات ورفعها في معرض اعمال الفري لانسر    

plt.savefig('top_product_chart.png', bbox_inches='tight')
plt.show()
