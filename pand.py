import pandas as pd
import numpy as np

# data = np.array([[1,2,3],[2,3,34],[3,5,76]])
# flat_data = data.flatten()
# print(flat_data)
# s1 = pd.Series(flat_data)
# print(s1)

# a = pd.array([2,3,4,54,5,6,6])

# s = pd.Series([[1,2,3,4,5,6,7],[0,1,3,4,5,6,8],[2,3,4,5,6,7,8]])

# df = pd.DataFrame({'A':[1,2,3],'B':[2,6,7],'C':[1,2,3]})
# print(s)

# print(df)

# print(a)

# array = [1,2,3,4,5,66,7,7,5,5,3,'🐶','🐱']
# array_2D = [[2,3,4,23],[32,34,3,4],[5,3,4,6],[2,3,4,2]]

# s = pd.Series(array)
# s1 = s.to_frame()
# s2 = s.tolist()
# s3 = s.astype(dtype=int)
# s4 = s.convert_dtypes()

#simple funcations
# print(s)
# print(s1)
# print(s2)
# print(s3)
# print(s.head("till number"))
# print(s.tail("till number from below"))

# print(s.info())
# print(s.values)
# print(s.index)
# print(s.name)
# print(s.size)
# print(s.shape())
# print(s.describe)

#missing Data Handling
# print(s.isna())
# print(s.notna())

# print(s.dropna())
# print(s.fillna(6))
# print(s.bfill())
# print(s.interpolate())
# print(s.replace)

#Arithmetic Operations
# s2 = pd.Series(array)

# print(s.add(s2))
# print(s.div(s2))

# print(s.mod(s2))
# print(s.abs())
# print(s.clip(0,60)) # forcefully convert all data into this range
# print(s.eq(s2))
# print(s.ne(s2))

#Statistical Methods
# print(s.prod())
# print(s.min())
# print(s.max())
# print(s.median())
# print(s.mean())


#Differences
# print(s.diff())


#Unique and Sorting
# print(s.unique())
# print(s.nunique())
# print(s.argsort())
# print(s.sort_values())
# print(s.sort_index())

#Funcation Application
# print(s.map(lambda x: x**2))
# print(s.apply(lambda x:x*2))




# DATAFRAME
df = pd.read_csv('demo.csv')
df.to_csv('out.csv',index=False)

print(df.head())
print(df.tail(10))
print(df.describe())

# a = df.iloc[0:2,0:3]
# df.loc[2,'a']

a = df['Roll_number']
print(a)
