import pandas as pd
df=pd.read_csv("D:\Coding\College IITJ\BDA\Capstone\Datas\Purchase_Information(cleaned).csv")

# print(df.head())
# print(df['Amount'].dtype)
total = df['Amount'].sum()
print(f'The total spend is {total}')
No_customers=df["Transaction ID"].nunique()
print(f"The Total unique customers are {No_customers}")
average_spend=total/No_customers
print(f"The average spend is {average_spend}")
