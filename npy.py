import time
import math

def calc(Numerical):
  start = time.time()
  if type(Numerical) == list:Numbers = Numerical
  elif type(Numerical) == str:Numbers = eval(Numerical)
  else:Numbers = Numerical
  data = sorted(Numbers)
  half = len(data) // 2
  box, Outlier = [], []
  Sum, Record, Total, Range25per, max_count = 0, 0, 0, 0, 0
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
  Min_value, Max_value = data[0], data[len(data)-1]
  Len = len(data)
  mode_value = None
  for d in data:
    data_count = data.count(d)
    if data_count > max_count:max_count, mode_value = data_count, d
  end = time.time()
  TaskTime = end - start
  result = {
    'len': Len,
    'average': Average,
    'max': Max_value,
    'min': Min_value,
    'median': Range50per,
    'Q1': Range25per,
    'Q2': Range50per,
    'Q3': Range75per,
    'IQR': Quartilerange,
    'range': Scope,
    'mode': mode_value,
    'outliers': Outlier,
    'task_time': TaskTime
  }
  return result

def calc2data(data):
  start = time.time()
  if type(data) == list:num_data, data_type = data, list
  elif type(data) == str:num_data, data_type = eval(data), str
  else:num_data, data_type = data, None
  sorted_data, total,deviation_total = sorted(num_data), 0 , 0
  for value in sorted_data:total += value
  average = total / len(sorted_data)
  deviation_list,output_deviation,deviation_squared_list = [],[],[]
  for value in sorted_data:
    deviation = value - average
    deviation_list.append(deviation)
    output_deviation.append(f"({value}-{average})²")
    deviation_squared = deviation * deviation
    deviation_squared_list.append(deviation_squared)
    deviation_total += deviation_squared
  variance = deviation_total / len(sorted_data)
  deviation_str = '+'.join(output_deviation)
  data_len = len(sorted_data)
  standard_deviation = math.sqrt(variance)
  end = time.time()
  TaskTime = end - start
  result = {
    'average': average,
    'variance': variance,
    'standard_deviation': standard_deviation,
    'len': data_len,
    'deviation_str': deviation_str,
    'data_type': data_type,
    'TaskTime': TaskTime
  }
  return result
