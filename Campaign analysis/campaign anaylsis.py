import pandas as pd
import matplotlib.pyplot as plt

df1=pd.read_csv("D:\Coding\College IITJ\BDA\Capstone\Datas\Purchase_Information(cleaned).csv")
df2=pd.read_excel("D:\Coding\College IITJ\BDA\Capstone\Datas\Discount_Information.xlsx")

df1["Transaction Date"] = pd.to_datetime(df1["Transaction Date"], format="%Y-%m-%d")

print(df1["Discount Code"].count())
print(df2["Discount Code"].count())

