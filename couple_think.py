import thinks
import couple_csv_data_list
import think_range
import return_file_csv_list
import return_file_path
import pprint

# numfour_heart = return_file_csv_list.heart_data(return_file_path.numfour_heart()[1])
# numfour_active = return_file_csv_list.return_file_csv_data_list(return_file_path.numfour_active()[1])
# numfive_heart = return_file_csv_list.heart_data(return_file_path.numfive_heart()[1])
# numfive_active = return_file_csv_list.return_file_csv_data_list(return_file_path.numfive_active()[1])

def change_time(t):
  if t[0] == '0':
    t = list(t)
    t = t.pop(0)
    t = ''.join(t)
  return t

# 1
def heart_suit_time(numfour, numfive):
  hako = 0
  heart_suit_row = []
  for row in range(len(numfour)):
    try:
      hako = numfour[row][3]
      hako = numfive[row][3]
      heart_suit_row.append(change_time(numfour[row][0]))
    except:
      continue
  return heart_suit_row 

# 2
def active_suit_time(numfour, numfive):
  numfour_time_list = []
  numfive_time_list = []
  for row in numfour:
    numfour_time_list.append(row[0])
  for row in numfive:
    numfive_time_list.append(row[0])
  both_active = set(numfour_time_list) & set(numfive_time_list)
  return both_active
  
# 3
# couple_both_suit_time(couple_heart_suit_time(numfour, numfive), couple_active_time(numfour, numfive))
def both_suit_time(heart_suit, active_suit):
  return set(heart_suit) & set(active_suit)

def active_suit_time_data(numfour, numfive):
  both_suit_time = active_suit_time(numfour, numfive)
  numfour_list = []
  numfive_list = []
  four_time_list = []
  five_time_list = []
  active_suit_data = []
  for row in numfour:
   four_time_list.append(row[0]) 
  for row in numfive:
    five_time_list.append(row[0])
  
  four_data = [] 
  five_data = []
  for row in both_suit_time:
    four_data.append(four_time_list.index(row))
    five_data.append(five_time_list.index(row))
  for row in four_data:
    numfour_list.append(numfour[row])
  for row in five_data:
    numfive_list.append(numfive[row])
  active_suit_data.append(numfour_list)
  active_suit_data.append(numfive_list)
  return active_suit_data

# 4, 5, 6
def active_type_time(numfour, numfive, life_type):
  data = active_suit_time_data(numfour, numfive)
  count = 0
  for row in data[0]:
    if row[2] == life_type:
      count += 1
  for row in data[1]:
    if row[2] == life_type:
      count += 1
  
  return count

# 7 8 9
def both_suit_type(numfour_heart, numfour_active, numfive_heart, numfive_active, life_type):
  heart_suit = heart_suit_time(numfour_heart, numfive_heart)
  active_suit = active_suit_time(numfive_heart, numfive_active)
  both_suit = both_suit_time(heart_suit, active_suit)
  four_time = []
  five_time = []
  four_data = []
  five_data = []
  count = 0
  
  for row in numfour_active:
    four_time.append(row[0])
  for row in numfive_active:
    five_time.append(row[0])

  for row in both_suit:
    row = change_time(row)
    five_data.append(numfive_active[five_time.index(row)])
    
  for row in four_data:
    if row[2] == life_type:
      count += 1 
  for row in five_data:
    if row[2] == life_type:
      count += 1

  return count 

# 10
def both_met_average(numfour_heart, numfour_active, numfive_heart, numfive_active):
  heart_suit = heart_suit_time(numfour_heart, numfive_heart)
  active_suit = active_suit_time(numfour_active, numfive_active)
  both_suit = both_suit_time(heart_suit, active_suit)
  four_time = []
  five_time = []
  four_data = []
  five_data = []

  for row in numfour_active:
    four_time.append(row[0])
  for row in numfive_active:
    five_time.append(row[0])

  for row in both_suit:
    four_data.append(numfour_active[four_time.index(row)])
    five_data.append(numfive_active[five_time.index(row)])

  total = 0
  count = 0
  for row in four_data:
    if float(row[1]) == 0:
      continue
    else:
      total += float(row[1])
      count += 1
  for row in five_data:
    if float(row[1]) == 0:
      continue
    else:
      total += float(row[1])
      count += 1 
  return total/count

# 11 
def both_heart_average(numfour_heart, numfour_active, numfive_heart, numfive_active):
  heart_suit = heart_suit_time(numfour_heart, numfive_heart)
  active_suit = active_suit_time(numfour_active, numfive_active)
  both_suit = both_suit_time(heart_suit, active_suit)
  four_time = []
  five_time = []
  four_data = []
  five_data = []

  for row in numfour_active:
    four_time.append(row[0])
  for row in numfive_active:
    five_time.append(row[0])

  for row in both_suit:
    four_data.append(numfour_active[four_time.index(row)])
    five_data.append(numfive_active[five_time.index(row)]) 
  
  total = 0
  count = 0
  for row in four_data:
    try:
      total += float(row[3])
      count += 1
    except:
      continue
  for row in five_data:
    try:
      total += float(row[3])
      count += 1
    except:
      continue
  return total/count

# 12 13 16
def both_heart_average_type(numfour_heart, numfour_active, numfive_heart, numfive_active, life_type):
  heart_suit = heart_suit_time(numfour_heart, numfive_heart)
  active_suit = active_suit_time(numfour_active, numfive_active)
  both_suit = both_suit_time(heart_suit, active_suit)
  four_time = []
  five_time = []
  four_data = []
  five_data = []

  for row in numfour_active:
    four_time.append(row[0])
  for row in numfive_active:
    five_time.append(row[0])

  for row in both_suit:
    four_data.append(numfour_active[four_time.index(row)])
    five_data.append(numfive_active[five_time.index(row)]) 
  
  total = 0
  count = 0
  for row in four_data:
    if row[2] == life_type:
      try:
        total += float(row[3])
        count += 1
      except:
        continue
  for row in five_data:
    if row[2] == life_type: 
      try:
        total += float(row[3])
        count += 1
      except:
        continue
  return total/count

# 14 15
def both_met_average_type(numfour_heart, numfour_active, numfive_heart, numfive_active, life_type):
  heart_suit = heart_suit_time(numfour_heart, numfive_heart)
  active_suit = active_suit_time(numfour_active, numfive_active)
  both_suit = both_suit_time(heart_suit, active_suit)
  four_time = []
  five_time = []
  four_data = []
  five_data = []

  for row in numfour_active:
    four_time.append(row[0])
  for row in numfive_active:
    five_time.append(row[0])

  for row in both_suit:
    four_data.append(numfour_active[four_time.index(row)])
    five_data.append(numfive_active[five_time.index(row)])

  total = 0
  count = 0
  for row in four_data:
    if row[2] == life_type:
      if float(row[1]) == 0:
        continue
      else:
        total += float(row[1])
        count += 1
  for row in five_data:
    if row[2] == life_type:
      if float(row[1]) == 0:
        continue
      else:
        total += float(row[1])
        count += 1 
  return total/count

# 17
def total_mets(numfour_active, numfive_active):
  total = 0
  for row in numfour_active:
    total += float(row[1])
  for row in numfive_active:
    total += float(row[1])
  return total

def both_mets_total(numfour_heart, numfour_active, numfive_heart, numfive_active):
  heart_suit = heart_suit_time(numfour_heart, numfive_heart)
  active_suit = active_suit_time(numfour_active, numfive_active)
  both_suit = both_suit_time(heart_suit, active_suit)
  four_time = []
  five_time = []
  four_data = []
  five_data = []

  for row in numfour_active:
    four_time.append(row[0])
  for row in numfive_active:
    five_time.append(row[0])

  for row in both_suit:
    four_data.append(numfour_active[four_time.index(row)])
    five_data.append(numfive_active[five_time.index(row)]) 
  
  total = 0
  count = 0
  for row in four_data:
    try:
      total += float(row[3])
    except:
      continue
  for row in five_data:
    try:
      total += float(row[3])
    except:
      continue 
  return total

# print(both_heart_average(numfour_heart, numfour_active, numfive_heart, numfive_active))
# print(both_heart_average_type(numfour_heart, numfour_active, numfive_heart, numfive_active, '生活活動'))
# print(both_met_average_type(numfour_heart, numfour_active, numfive_heart, numfive_active, '生活活動'))
# print(total_mets(numfour_active, numfive_active))
# print(both_mets_total(numfour_heart, numfour_active, numfive_heart, numfive_active))
