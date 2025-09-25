import pandas as pd
import numpy as np
df=pd.read_excel('D:\Coding\College IITJ\BDA\Capstone\Purchase_Information.xlsx')
print(df.head())
print(df.isnull().sum())
df.loc[13,"Transaction Date"]="19/01/2025" # Changed to dd/mm/yyyy format
df.loc[12,"Transaction Date"]="18/01/2025"
df.loc[32,"Transaction Date"]="08/02/2025"
print(df["Transaction Date"])
print(df.describe())
print(df.info())

df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], format='%d/%m/%Y')



df["Discount Code"]=df["Discount Code"].replace(".", np.nan)
print(df.isnull().sum())
df.to_csv("Purchase_Information(cleaned).csv",index=False)
print(df.info())
df.to_excel("Purchase_Information (cleaned).xlsx")

df=pd.read_excel('D:\Coding\College IITJ\BDA\Customer_Information.xlsx')
df["city"] = df["city"].str.title()

df.to_csv("Customer_Information (cleaned).csv")
