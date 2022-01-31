import pandas as pd

df = pd.read_csv("/home/bhavik/Downloads/FoodBalanceSheets_E_Africa_NOFLAG.csv")
print(df)
print(df.groupby("Item").sum())
print(df.descrihttps://github.com/jain-bhakti/Hamoye-data-science-internship-codebe())
print(df.isnull().sum())
print(df.corr())
print(df.groupby("Element").sum())
print(df["Area"].unique())
