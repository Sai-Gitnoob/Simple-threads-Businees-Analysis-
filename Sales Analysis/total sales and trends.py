import pandas as pd
import matplotlib.pyplot as plt

df1=pd.read_csv("D:\Coding\College IITJ\BDA\Capstone\Datas\Purchase_Information(cleaned).csv")
df2=pd.read_excel("D:\Coding\College IITJ\BDA\Capstone\Datas\Product_Information (cleaned).xlsx")
df1["Transaction Date"] = pd.to_datetime(df1["Transaction Date"], format="%Y-%m-%d")
# print(df1.head())
# print(df2.head())
df1_sample=df1.head(15)
df2_sample=df2.head(15)
df_merged= pd.merge(df1_sample,df2_sample,on="Product ID",how="inner")
daily_sales = df_merged.groupby("Transaction Date")["Amount"].sum().reset_index()
print(df_merged.head())
xaxis1=daily_sales["Transaction Date"].dt.strftime("%d-%m")
yaxis2=daily_sales["Amount"]
plt.plot(xaxis1,yaxis2,marker="o", linestyle="-")
plt.title ("Trend of sales for 15 days ")
plt.xlabel("Day")
plt.ylabel("Sales amount")
plt.show()

