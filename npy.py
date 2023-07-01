import time
import math

def calc(data):
  start = time.time()
  if type(data) == list:data = data
  elif type(data) == str:data = eval(data)
  sorted_data = sorted(data)
  half = len(sorted_data) // 2
  box, Outlier = [], []
  Sum, Record, Total, Range25per, max_count , mode_value = 0,0,0,0,0,None
  for i in range(len(sorted_data)):Total += sorted_data[i]
  Average = Total / len(sorted_data)
  for number in range(len(sorted_data)):
    if Average * 3 <= sorted_data[number]:
      Outlier.append(sorted_data[number])
  if len(sorted_data) % 2 == 0:Range50per = (sorted_data[half - 1] + sorted_data[half]) / 2
  else:Range50per = sorted_data[half]
  if (half / 2).is_integer():
    for i in range(half):
      if i == (half // 2) - 1:Sum += sorted_data[i]
      elif i == half // 2:Sum += sorted_data[i]
    Range25per = Sum / 2
    for j in range(len(sorted_data)):
      if j >= half + 1:
        box.append(sorted_data[j])
        Record += 1
    Range75per = (box[Record // 2] + box[(Record // 2) - 1]) / 2
  else:
    for i in range(half):
      if i == half // 2:Range25per += sorted_data[i]
    for j in range(len(sorted_data)):
      if j >= half:
        box.append(sorted_data[j])
        Record += 1
    Range75per = box[Record // 2]
  Scope = sorted_data[len(sorted_data)-1] - sorted_data[0]
  Quartilerange = Range75per - Range25per
  Min_value, Max_value = sorted_data[0], sorted_data[len(sorted_data)-1]
  Len = len(sorted_data)
  for d in sorted_data:
    data_count = sorted_data.count(d)
    if data_count > max_count:max_count,mode_value = data_count,d
  end = time.time()
  TaskTime = end - start
  result = {
    'len': Len,
    'average': Average,
    'max': Max_value,
    'min': Min_value,
    'median': Range50per,
    'IQR': Quartilerange,
    'range': Scope,
    'mode': mode_value,
    'outliers': Outlier,
    'Q1': Range25per,
    'Q2': Range50per,
    'Q3': Range75per,
    'Q': {
      'Q1': Range25per,
      'Q2': Range50per,
      'Q3': Range75per
    },
    'task_time': TaskTime
  }
  return result

def Difference(data):
  start = time.time()
  if type(data) == list:data, data_type = data,list
  elif type(data) == str:data, data_type = eval(data),str
  else:data, data_type = data, None
  sorted_data, total,deviation_total = sorted(data),0,0
  for value in sorted_data:total += value
  average = total / len(sorted_data)
  deviation_list,output_deviation,deviation_squared_list = [],[],[]
  for value in sorted_data:
    deviation = value - average
    deviation_list.append(deviation)
    output_deviation.append(f'({value}-{average})²')
    deviation_squared = deviation * deviation
    deviation_squared_list.append(deviation_squared)
    deviation_total += deviation_squared
  variance = deviation_total / len(sorted_data)
  deviation_str = '+'.join(output_deviation).replace('.0','')
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

def merge(x,y):
  deviation1st,Quartile1st = Difference(x),calc(x)
  deviation2nd,Quartile2nd = Difference(y),calc(y)
  result = {
    'deviation[1]':deviation1st,
    'Quartile[1]':Quartile1st,
    'deviation[2]':deviation2nd,
    'Quartile[2]':Quartile2nd
  }
  return result

def prime(start,end):
  number = range(start,end)
  def prime(num):
    for x in range(2,num):
      if (num % x) == 0:
        return False
    return True
  primes = list(filter(prime,number))
  result = {
    'primes': primes,
    'start_num': start,
    'end_num': end
  }
  return result
