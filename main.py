import pandas
a = ["d", 'x', 'l', 'q']
b = ["d", 'x', 'l', 'q']
myser = pandas.Series(a)
mydf = pandas.DataFrame([a, b], columns=['11', '22', '33', '44'], index=[1, 2])
print(myser)
print(mydf)
print('')
# print(mydf[1])
