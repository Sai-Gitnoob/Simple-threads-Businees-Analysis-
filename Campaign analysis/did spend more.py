"""
Lets answer the question do the people with discount coupons spend more 
than those who didnt have any
"""

import pandas as pd
import matplotlib.pyplot as plt

df1=pd.read_csv("D:\Coding\College IITJ\BDA\Capstone\Datas\Purchase_Information(cleaned).csv")
df2=pd.read_excel("D:\Coding\College IITJ\BDA\Capstone\Datas\Product_Information (cleaned).xlsx")
df1["Transaction Date"] = pd.to_datetime(df1["Transaction Date"], format="%Y-%m-%d")

discount_used=df1[df1["Discount Code"].notnull()]
print(discount_used)
count=(discount_used["Transaction ID"].count())
discount_not_used=df1[df1["Discount Code"].isnull()]
print(discount_not_used)
count2=(discount_not_used["Transaction ID"].count())

joined = pd.merge(discount_used, df2, on="Product ID", how="inner")
joined2 = pd.merge(discount_not_used, df2, on="Product ID", how="left")
# print(joined)

total_dis_spend=joined["Price(INR)"].sum()
print(total_dis_spend)


total_nondis_spend=joined2["Amount"].sum()
print(total_nondis_spend)


average_spend_dis=total_dis_spend/count
average_spend_not_dis=total_nondis_spend/count2
print(average_spend_dis)
print(average_spend_not_dis)




