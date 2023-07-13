from npy import merge

x = input("データ1:")
y = input("データ2:")

data = merge(x,y)
print(data)
print(data["Quartile[1]"]["range"])
