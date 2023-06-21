numbers = [100,4,1,9,12,52,58,88,10,25,300,29,63,71,22,11,35,39,8,41,45,6,9]
data = sorted(numbers)
half = len(data) // 2
box,outlier = [],[]
num,count,total,quartile1 = 0,0,0,0

for i in range(0,len(data)):
  total += data[i]
value = round(total / len(data),1)

for number in range(0,len(data)):
  if (value * 3) <= data[number]:
    outlier.append(data[number])

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
