import pandas as pd


# data1 = {
#     "name" : ["Sufyan","Afzal","Malik"],
#     "sport" : ["Football","Cricket","Wrestling"],
#     "gender" : ["M","M","M"]
# }

# df = pd.DataFrame(data1)
# print(df.head())   # print(df.head(2))
# print(df.shape)
# print(df.shape[0])
# print(df.shape[1])
# print(df.tail())


# df1 = pd.DataFrame(data1, columns=["name","sport"])
# print(df1)


# df2 = pd.DataFrame(data1, columns=["name","sport"],index=["pehla","doosra","teesra"])
# print(df2)
# print(df2["sport"])
# print(df2.loc[["doosra"]])
# print(df2.loc[["doosra","teesra"]])


# df3 = pd.DataFrame(data1, columns=["name","sport"])
# values3 = [24,50,100]
# df3["age"] = values3
# # print(df3)
# # print(df3["age"])
# df3["umar daraz"] = df3["age"]>=25
# print(df3["umar daraz"])



# obj1 = pd.Series([1,"John",3.5,"Bismillah"])
# print(obj1)
# print(obj1.values)


# obj2 = pd.Series([2,"Sena",3.9,"You can't see me"], index=["nela","peela","sharmeela","phurteela"])
# print(obj2)
# print(obj2["sharmeela"])


# dataset1 = pd.read_csv("Lab 4/House_Rent_Dataset.csv", sep=',')
# print(dataset1)
# print(dataset1.dtypes)
# print(dataset1.columns)
# print(dataset1.head())
# print(dataset1['City'].describe())
# print(dataset1['City'].value_counts())
# print(dataset1['City'].unique())
# print(pd.crosstab(dataset1['City'],dataset1['Floor']))
# print(dataset1['Size'].mean())



# house_details = pd.read_csv("Lab 4/House_Rent_Dataset.csv", sep=',')
# print(house_details)

