import math

def calc(data):
  if type(data) == str:
    data = data.strip('[]').split(',')
    data = [float(x) for x in data]
  sorted_data = sorted(data)
  half = len(sorted_data) // 2
  box, Outlier = [], []
  Sum, Record, Total, Range25per, max_count, mode_value = 0,0,0,0,0,None
  for i in range(len(sorted_data)):Total += sorted_data[i]
  Average = Total / len(sorted_data)
  for number in range(len(sorted_data)):
    if Average * 3 <= sorted_data[number]:
      Outlier.append(sorted_data[number])
  if len(sorted_data) % 2 == 0: Range50per = (sorted_data[half - 1] + sorted_data[half]) / 2
  else: Range50per = sorted_data[half]
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
  Scope = sorted_data[len(sorted_data) - 1] - sorted_data[0]
  Quartilerange = Range75per - Range25per
  Min_value, Max_value = sorted_data[0], sorted_data[len(sorted_data) - 1]
  Len = len(sorted_data)
  for d in sorted_data:
    data_count = sorted_data.count(d)
    if data_count > max_count:max_count,mode_value = data_count,d
  result = {
    'len': Len,
    'Total': Total,
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
    }
  }
  return result

def Difference(data):
  if type(data) == str:
    data = data.strip('[]').split(',')
    data = [float(x) for x in data]
  deviation_list,deviation_squared_list = [],[]
  sorted_data, total,deviation_total = sorted(data),0,0
  data_len = len(sorted_data)
  for value in sorted_data:total += value
  average = total / data_len
  for value in sorted_data:
    deviation = value - average
    deviation_list.append(deviation)
    deviation_squared = deviation ** 2
    deviation_squared_list.append(deviation_squared)
    deviation_total += deviation_squared
  variance = deviation_total / data_len
  standard_deviation = math.sqrt(variance)
  result = {
    'sorted_data': sorted_data,
    'total':total,
    'len': data_len,
    'average': average,
    'variance': variance,
    'deviation_list': deviation_list,
    'standard_deviation': standard_deviation,
    'deviation_squared_list': deviation_squared_list,
  }
  return result

def merge(x,y):
  difference1st,Quartile1st = Difference(x),calc(x)
  difference2nd,Quartile2nd = Difference(y),calc(y)
  result = {
    'data[1]': {
      'Quartile': Quartile1st,
      'deviation': difference1st,
    },
    'data[2]': {
      'Quartile': Quartile2nd,
      'deviation': difference2nd,
    },
  }
  return result

def prime_numbers(start, end):
  numbers = range(start, end + 1)
  def is_prime(num):
    if num <= 1: return False
    for x in range(2, int(math.sqrt(num)) + 1):
      if (num % x) == 0: return False
    return True
  primes = list(filter(is_prime, numbers))
  result = {
    'primes': primes,
    'start_num': start,
    'end_num': end,
  }
  return result
