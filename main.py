from npy import calc,calc2data
data1 = [1,2,3,4,5] # or data1 = "1,2,3,4,5"
data2 = [5,6,8,5,7] # or data2 = "5,6,8,5,7"

data1resp = calc2data(data1)
data2resp = calc2data(data2)
print(f"分散(s²) = {data1resp['variance']}\n標準偏差 = √{data1resp['standard_deviation']}")
print(f"分散(s²) = {data2resp['variance']}\n標準偏差 = √{data2resp['standard_deviation']}")
print(f"Data1: 平均 = {data1resp['average']:.2f}, 分散 = {data1resp['variance']:.2f}, 標準偏差 = {data1resp['standard_deviation']:.2f}")
print(f"Data2: 平均 = {data2resp['average']:.2f}, 分散 = {data2resp['variance']:.2f}, 標準偏差 = {data2resp['standard_deviation']:.2f}")
result = calc(data1)
print('平均値:', result['average'])
print('最大値:', result['max'])
print('最小値:', result['min'])
print('中央値:', result['median'])
print('第1四分位数:', result['Q1'])
print('第2四分位数:', result['Q2'])
print('第3四分位数:', result['Q3'])
print('四分位範囲:', result['IQR'])
print('範囲:', result['range'])
print('最頻値:', result['mode'])
print('外れ値:', result['outliers'])
print('処理時間:', result['task_time'])
