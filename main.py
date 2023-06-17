numbers = [1,2,3,4,5,6]
data = sorted(numbers)
half = len(data) // 2
num,count,Total,quartile1 = 0,0,0,0
box = []
for i in range(0,len(data)):
  Total += data[i]
value = Total / len(data)

if len(data) % 2 == 0:
  median = (data[half - 1] + data[half]) / 2
else:
  median = data[half]

if (half / 2).is_integer():
  for i in range(half):
    if i == (half // 2) - 1:
      num += data[i]
    elif i == half // 2:
      num += data[i]
  quartile1 = num / 2
  for j in range(len(data)):
    if j >= half + 1:
      box.append(data[j])
      count += 1
  quartile3 = (box[count // 2] + box[(count // 2) - 1]) / 2
else:
  for i in range(half):
    if i == (half // 2):
      quartile1 += data[i]
  for j in range(len(data)):
    if j >= half:
      box.append(data[j])
      count += 1
  quartile3 = box[count // 2]
