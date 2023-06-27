import time
def Main(Numerical):
  global Numbers,data,Total,mode
  global Range25per,Range50per,Range75per
  global Outlier,Scope,Quartilerange
  global Average,Max,Min,Len,Record,half,Type
  global TaskTime
  start = time.time()
  if type(Numerical) == list:Numbers,Type = Numerical,list
  elif type(Numerical) == str:Numbers,Type = eval(Numerical),str
  else:Numbers,Type = Numerical,None
  data = sorted(Numbers)
  half = len(data) // 2
  box,Outlier = [],[]
  Sum,Record,Total,Range25per,max = 0,0,0,0,0
  for i in range(len(data)):Total += data[i]
  Average = Total / len(data)
  for number in range(len(data)):
    if Average * 3 <= data[number]:Outlier.append(data[number])
  if len(data) % 2 == 0:Range50per = (data[half - 1] + data[half]) / 2
  else:Range50per = data[half]
  if (half / 2).is_integer():
    for i in range(half):
      if i == (half // 2) - 1:Sum += data[i]
      elif i == half // 2:Sum += data[i]
    Range25per = Sum / 2
    for j in range(len(data)):
      if j >= half + 1:
        box.append(data[j])
        Record += 1
    Range75per = (box[Record // 2] + box[(Record // 2) - 1]) / 2
  else:
    for i in range(half):
      if i == half // 2:Range25per += data[i]
    for j in range(len(data)):
      if j >= half:
        box.append(data[j])
        Record += 1
    Range75per = box[Record // 2]
  Scope = data[len(data)-1] - data[0]
  Quartilerange = Range75per - Range25per
  Min,Max = data[0],data[len(data)-1]
  Len = len(data)
  for d in data:
    data_count = data.count(d)
    if data_count > max:max,mode = data_count,d
  end = time.time()
  TaskTime = end - start
