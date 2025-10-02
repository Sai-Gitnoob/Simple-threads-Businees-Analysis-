import pandas as pd
import matplotlib.pyplot as plt

df1=pd.read_csv("D:\Coding\College IITJ\BDA\Capstone\Datas\Purchase_Information(cleaned).csv")
df2=pd.read_excel("D:\Coding\College IITJ\BDA\Capstone\Datas\Discount_Information.xlsx")
df1["Transaction Date"] = pd.to_datetime(df1["Transaction Date"], format="%Y-%m-%d")
print(df2.head())
count_per_coupon=df1["Discount Code"].value_counts()
most_used_coupon=count_per_coupon.index[0]
count_most =count_per_coupon.iloc[0]
print(f"As per the number of columns the count are\n {count_per_coupon}")

print("Thus the most used coupon in the sales is ",most_used_coupon,"with count",count_most)
