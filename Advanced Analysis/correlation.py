import pandas as pd
df=pd.read_csv("D:\Coding\College IITJ\BDA\Capstone\Datas\Purchase_Information(cleaned).csv")
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], format="%Y-%m-%d")
df1=pd.read_excel("D:\Coding\College IITJ\BDA\Capstone\Datas\Discount_Information.xlsx")
print(df1.head())
newdf=pd.merge(df1,df,on="Discount Code",how="left")
print(newdf["Discount Code"])
print(newdf["Transaction ID"])
print(newdf["Discount percentage"])

df.to_excel("Correlation Df.xlsx")

# import pandas as pd

# df1 = pd.read_csv("D:\Coding\College IITJ\BDA\Capstone\Datas\Purchase_Information(cleaned).csv")
# df2 = pd.read_excel("D:\Coding\College IITJ\BDA\Capstone\Datas\Discount_Information.xlsx")

# merged_df = pd.merge(df1, df2, on="Discount Code", how="left")

# print(merged_df.head())



