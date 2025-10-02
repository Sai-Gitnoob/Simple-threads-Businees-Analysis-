import pandas as pd
import matplotlib.pyplot as plt

df1=pd.read_csv("D:\Coding\College IITJ\BDA\Capstone\Datas\Purchase_Information(cleaned).csv")
df2=pd.read_excel("D:\Coding\College IITJ\BDA\Capstone\Datas\Product_Information (cleaned).xlsx")
df1["Transaction Date"] = pd.to_datetime(df1["Transaction Date"], format="%Y-%m-%d")

joined_data=pd.merge(df1,df2,on="Product ID")
print(joined_data.head(10))

category_revenue = joined_data.groupby("Product Name")["Amount"].sum()

plt.pie(
    category_revenue.values, 
    labels=category_revenue.index, 
    autopct='%1.1f%%',  # show percentages
    startangle=140      # for better layout
)
plt.title("Revenue Contribution by Product Category")
plt.show()