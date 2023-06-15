numbers = [1,5,8,5,6,4,9,1,1]
data = sorted(numbers)
half = len(data) // 2
number1 = 0
number2 = 0
if (half / 2).is_integer():
  for i in range(half):
    if i == (half // 2) - 1:
      number1 += data[i]
    elif i == half // 2:
      number2 += data[i]
  quartile1 = (number1 + number2) / 2
  box = []
  count = 0
  for j in range(len(data)):
    if j >= half + 1:
      box.append(data[j])
      count += 1
  quartile3 = (box[count // 2] + box[(count // 2) - 1]) / 2
else:
  quartile1 = 0
  for i in range(half):
    if i == (half // 2):
      quartile1 += data[i]
  box = []
  count = 0
  for j in range(len(data)):
    if j >= half:
      box.append(data[j])
      count += 1
  quartile3 = box[count // 2]
if len(data) % 2 == 0:
  median = (data[half - 1] + data[half]) / 2
else:
  median = data[half]
Total = 0
for i in range(0,len(data)):
  Total += data[i]
Averagevalue = Total / len(data)
print("________________________")
print(f"元データ {numbers}\n降順 {data}")
print(f"Total{Total} ÷ リストの長さ({len(data)}) = 平均値({round(Averagevalue,1)})")
print(f"中央値 {median}")
print(f"第1四分位数 {quartile1}\n第2四分位数 {median}\n第3四分位数 {quartile3}")
print(f"四分位範囲 ({quartile3} - {quartile1}) = {quartile3 - quartile1}")
print(f"範囲{data[len(data)-1]}-{data[0]}={data[len(data)-1] - data[0]}")
