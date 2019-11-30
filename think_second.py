import return_file_path
import return_file_csv_list
import couple_think

numfour_heart = return_file_csv_list.heart_data(return_file_path.numfour_heart()[1])
numfour_active = return_file_csv_list.return_file_csv_data_list(return_file_path.numfour_active()[1])

# 1
def heart_suit_time(num):
  hako = 0
  heart_suit_row = []
  for row in range(len(num)):
    try:
      hako = num[row][3]
      heart_suit_row.append(num[row][0])
    except:
      continue
  return heart_suit_row

# 2
def active_suit_time(num):
  numfour_time_list = []
  for row in num:
    numfour_time_list.append(row[0])
  return numfour_time_list 

# 3
def both_suit_time(heart_suit, active_suit):
  return set(heart_suit) & set(active_suit)

def active_suit_time_data(num):
  return num

# 4 5 6
def active_type_time(num, life_type):
  count = 0
  for row in num:
    if row[2] == life_type:
      count += 1
  return count
  
# 7 8 9
def both_suit_type(heart, active, life_type):
  heart_suit = heart_suit_time(heart)
  active_suit = active_suit_time(active)
  both_suit = both_suit_time(heart_suit, active_suit)
  four_time = []
  four_data = []
  count = 0
  
  for row in active:
    four_time.append(row[0])

  for row in both_suit:
    row = couple_think.change_time(row)
    four_data.append(active[four_time.index(row)])
    
  for row in four_data:
    if row[2] == life_type:
      count += 1 

  return count 

# 10
def both_met_average(heart, active):
  heart_suit = heart_suit_time(heart)
  active_suit = active_suit_time(active)
  both_suit = both_suit_time(heart_suit, active_suit)
  four_time = []
  four_data = []

  for row in active:
    four_time.append(row[0])

  for row in both_suit:
    four_data.append(active[four_time.index(row)])

  total = 0
  count = 0
  for row in four_data:
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








# active_suit_time(numfour_active)
# print(len(both_suit_time(heart_suit_time(numfour_heart), active_suit_time(numfour_active))))
# active_suit_time_data(numfour_active)
# print(active_type_time(numfour_active, '生活活動'))
# print(len(numfour_active))
# print(both_suit_type(numfour_heart, numfour_active, '生活活動'))
# print(both_met_average(numfour_heart, numfour_active))