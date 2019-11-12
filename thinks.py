def return_heart_counter_start_row(csv_data_list):
  for row in range(len(csv_data_list)):
    try:
      heart_counter_start_row = csv_data_list[row][3]
      heart_counter_start_row = row
      break
    except:
      continue
  return heart_counter_start_row

def return_heart_counter_finish_row(csv_data_list):
  for row in range(return_heart_counter_start_row(csv_data_list), len(csv_data_list)):
    try:
      heart_counter_start_row = csv_data_list[row][3]
    except:
      heart_counter_finish_row = row
      break
  return heart_counter_finish_row
  
# 1  
def return_heart_counter_suit_time(csv_data_list):
  heart_suit_time = return_heart_counter_finish_row(csv_data_list) - return_heart_counter_start_row(csv_data_list)  
  return heart_suit_time    
# 2
def return_active_counter_suit_time(start_row, finish_row):
  active_counter_suit_time = finish_row - start_row + 1
  return active_counter_suit_time

# 3
def return_both_counter_suit_time(csv_data_list, start_row, finish_row):
  both_suit_start_row = max(return_heart_counter_start_row(csv_data_list), start_row)
  both_suit_finish_row = min(return_heart_counter_finish_row(csv_data_list), finish_row)
  both_suit_time = both_suit_finish_row - both_suit_start_row 
  return both_suit_time 

# 4,5,6
def active_type_counter(csv_data_list, start_row, finish_row, active_type):
  active_type_counter = 0
  for row in range(start_row, finish_row + 1):
    if active_type == csv_data_list[row][2]:
      active_type_counter += 1
  return active_type_counter

# 7,8,9
def active_type_count_for_both_counter_suit(csv_data_list, start_row, finish_row, active_type):
  both_suit_start_row = max(return_heart_counter_start_row(csv_data_list), start_row)
  both_suit_finish_row = min(return_heart_counter_finish_row(csv_data_list), finish_row)
  total_count = 0
  for row in range(both_suit_start_row, both_suit_finish_row):
    if active_type == csv_data_list[row][2]:
      total_count += 1
  
  return total_count

# 10
def average_mets_count(csv_data_list, start_row, finish_row):      
  both_suit_start_row = max(return_heart_counter_start_row(csv_data_list), start_row)
  both_suit_finish_row = min(return_heart_counter_finish_row(csv_data_list), finish_row)
  average_mets = 0  
  row_count = 0
  for row in range(both_suit_start_row, both_suit_finish_row):
    if float(csv_data_list[row][1]) != 0:
      average_mets += float(csv_data_list[row][1])
      row_count += 1

  average_count = average_mets / row_count

  return average_count
# 11  
def average_heart_count(csv_data_list, start_row, finish_row):
  both_suit_start_row = max(return_heart_counter_start_row(csv_data_list), start_row)
  both_suit_finish_row = min(return_heart_counter_finish_row(csv_data_list), finish_row)
  average_heart_count = 0
  row_count = 0
  for row in range(both_suit_start_row, both_suit_finish_row):
    average_heart_count += float(csv_data_list[row][3])
    row_count += 1
  average_heart_count = average_heart_count / row_count
  return average_heart_count

# 12,13
def average_heart_count_for_active_type(csv_data_list, start_row, finish_row, active_type):
  both_suit_start_row = max(return_heart_counter_start_row(csv_data_list), start_row)
  both_suit_finish_row = min(return_heart_counter_finish_row(csv_data_list), finish_row)
  average_heart_count = 0
  row_count = 0

  for row in range(both_suit_start_row, both_suit_finish_row):
    if active_type == csv_data_list[row][2]:
      average_heart_count += float(csv_data_list[row][3])
      row_count += 1

  average_heart_count = average_heart_count / row_count 
  return average_heart_count

# 14,15
def average_mets_count_for_avtive_type(csv_data_list, start_row, finish_row, active_type):
  both_suit_start_row = max(return_heart_counter_start_row(csv_data_list), start_row)
  both_suit_finish_row = min(return_heart_counter_finish_row(csv_data_list), finish_row) 
  average_count = 0
  row_count = 0

  for row in range(both_suit_start_row, both_suit_finish_row):
    if active_type == csv_data_list[row][2]:
      average_count += float(csv_data_list[row][1])
      row_count += 1
    
  average_count = average_count / row_count
  return average_count

# 16
def average_heart_count_for_not_active(csv_data_list):
  start_row = return_heart_counter_start_row(csv_data_list)
  finish_row = return_heart_counter_finish_row(csv_data_list)
  total_heart_count = 0
  row_count= 0
  for row in range(start_row, finish_row):
    if csv_data_list[row][2] == '計測なし':
      total_heart_count += float(csv_data_list[row][3])
      row_count += 1
  average_heart_count = total_heart_count / row_count    
  return average_heart_count

# 17
def total_active_count(csv_data_list):
  total_active_count = 0
  for row in range(4, len(csv_data_list)):
    total_active_count += float(csv_data_list[row][1])
  return total_active_count
       
# 18
def both_counter_suit_total_active_count(csv_data_list, start_row, finish_row):
  both_suit_start_row = max(return_heart_counter_start_row(csv_data_list), start_row)
  both_suit_finish_row = min(return_heart_counter_finish_row(csv_data_list), finish_row) 
  total_active_count = 0

  for row in range(both_suit_start_row, both_suit_finish_row):
    total_active_count += float(csv_data_list[row][1])
  return total_active_count 