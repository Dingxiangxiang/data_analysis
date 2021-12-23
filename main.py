import pandas as pd
a = ["d", 'x', 'l', 'q']
b = ["d", 'x', 'l', 'q']
myser = pd.Series(a)
mydf = pd.DataFrame([a, b], columns=['11', '22', '33', '44'], index=[1, 2])
print("原始数据：")
print('series:\n', myser)
print('dataframe:\n', mydf)
print('series和dataframe 两种方式获取一行数据：')
print(mydf.loc[1])  # series
print(mydf.loc[[1]])  # dataframe

#
# 拼接
a1 = mydf.loc[[1]]
a2 = mydf.loc[[2]]
a3 = mydf.loc[1]
print("dataframe的三种拼接方式:")
print(mydf.append(a1))
print(mydf.append([a1, a2]))
print(mydf.append(a3))
print("原始表格不变")
print(mydf)

print('dataframe的初始化1：(这种缺省值用nan填充)')
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
print('dataframe的初始化2：')
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

# https://www.cnblogs.com/liulinghua90/p/9935642.html   pandas操作excel表格，需要安装xlrd模块 pip install xlrd
