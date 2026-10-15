import pandas as pd

df= pd.read_excel("sales_raw.xlsx")

# a=df.head()
# print(a)

df=df.drop_duplicates()
# a=df.duplicated().sum()
# print(a)

df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

df = df.dropna(subset=['Order_Date'])

# print(df)


df['Profit'] = df['Sales'] - df['Cost']
df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month
# print(df)

df.to_csv('sales_cleaned.csv',index=False)
