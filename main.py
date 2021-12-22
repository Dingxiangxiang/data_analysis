import pandas as pd
a = ["d", 'x', 'l', 'q']
b = ["d", 'x', 'l', 'q']
myser = pd.Series(a)
mydf = pd.DataFrame([a, b], columns=['11', '22', '33', '44'], index=[1, 2])
print(myser)
print(mydf)
print('')
print(mydf.loc[1])  # series
print(mydf.loc[[1]])  # dataframe

# data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
# df = pd.DataFrame(data)
# print(df)
#
# 拼接
a1 = mydf.loc[[1]]
a2 = mydf.loc[[1]]
a3 = mydf.loc[1]
# print(a1.append())


import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# 指定索引
print(df)
print(df.loc["day2"])
