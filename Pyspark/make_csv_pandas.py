import pandas as pd


# df = pd.read_excel('Pyspark/Online Retail.xlsx', dtype={'CustomerID': object})
# df.to_csv('Pyspark/Online_Retail.csv', index=False)
df = pd.read_csv('Pyspark/Online_Retail.csv', encoding='cp932')

# print(df.head())
# print(df.describe)
# print(df.shape)
# print(df.columns)
# print(df.dtypes)

# print(df[df.duplicated(keep="first")])  # "last" or False
# df.drop_duplicates(keep="first")
# df.drop_duplicates(subset="InvoiceNo", keep="first")  # columns set

# df.isnull().sum()
# # set the data to nan
# df.loc[1, "StockCode"] = np.nan
# # find the nan
# df.loc[df["StockCode"].isnull()]
# # delete data
# df.dropna(axis=0, how = "any")
# # delete columns
# df.dropna(subset=["StockCode"])
# # fill nan with 0
# df.fillna({"StockCode": 0})

# # change data type
# df.dtypes
# # InvoiceDate object
# df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], format="%Y-%m-%d %H:%M:%S")
# df.dtypes
# # InvoiceDate datetime64

# # take the hour of the datetime
# df["InvoiceDate"].dt.hour  # minute month time

# # 丸め
# df["InvoiceDate"].dt.round("D")  # H

# # do math with df
# df["Total"] = df["UnitPrice"] * df["Quantity"]
# df.head()

# # math the sale by day
# df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
# sales_1d = df.resample("D", on="InvoiceDate").sum()
# sales_1d = sales_1d.dorp(columns="CustomerID")
# print(sales_1d)

# # 移動平均
# sales_1d["3d_moving_avg"] = sales_1d["Total"].rolling(3).mean()
# sales_1d["3d_moving_avg_ctr"] = sales_1d["Total"].rolling(3, center=True).mean()
# print(sales_1d)

# # shift行方向にずらす
# sales_1d["3d_moving_avg_shift"] = sales_1d["3d_moving_avg"].shift(1)  # 1行をずらす

# # diff, pct_change
# sales_1d["diff"] = sales_1d["Total"].diff()
# sales_1d["pct_change"] = sales_1d["Total"].pct_change()
# print(sales_1d)

# join dataframe
# inner join left join
df_right = pd.DataFrame([[17850, "male", 30]], columns=["CustomerID", "sex", "age"])
print(df_right.dtypes)

df = df.fillna({"CustomerID": 9999})
df["CustomerID"] = df["CustomerID"].astype(int)
print(df.dtypes)

# inner join
df = pd.merge(df, df_right, how="inner", on="CustomerID")  # left join
print(df[df["CustomerID"] == 17850])
