import pandas as pd
df=pd.read_csv("Datas\Purchase_Information(cleaned).csv")

df["Transaction Date"]=pd.to_datetime(df["Transaction Date"])

print(df.head())


first_q= df[(df['Transaction Date'].dt.year==2025) & (df['Transaction Date'].dt.month<=3)]


unique = first_q["Transaction ID"].nunique()
print(f"The unique transactions in the first quarter are {unique}")

# # print(df.info())



