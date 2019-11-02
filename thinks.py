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
  
def return_heart_counter_suit_time(csv_data_list):
  heart_suit_time = return_heart_counter_finish_row(csv_data_list) - return_heart_counter_start_row(csv_data_list)  
  return heart_suit_time    

'''
def return_active_counter_suit_time(csv_data_list):
  active_count_start_time = 0
  finish_limit = 0
  active_count_finish_time = 0
  start_index_definition = 0  
  for row in range(4,len(csv_data_list)):
    if float(csv_data_list[row][1]) != 0:
      start_index_definition += 1

      # 0以外が10行続いたら行動計測定開始と判断
      if start_index_definition == 3:
        active_count_start_time = row 
        break

    else:
      start_index_definition = 0

  # 行動量計(1列目)の値で0が10行続いたら行動計測定は終了したと判断する
  for row in range(active_count_start_time, len(csv_data_list)):
    if float(csv_data_list[row][1]) == 0:
      finish_limit += 1
      if finish_limit == 60:
        active_count_finsh_time = row - 60 
        break
    else:
      finish_limit = 0
  return active_count_finish_time - active_count_start_time
'''

def return_active_counter_suit_time(start_row, finish_row):
  active_counter_suit_time = finish_row - start_row + 1
  return active_counter_suit_time

def return_both_counter_suit_time(csv_data_list, start_row, finish_row):
  both_suit_start_row = max(return_heart_counter_start_row(csv_data_list), start_row)
  both_suit_finish_row = min(return_heart_counter_finish_row(csv_data_list), finish_row)
  both_suit_time = both_suit_finish_row - both_suit_start_row 
  return both_suit_time 

def return_active_type_counter(csv_data_list, start_row, finish_row, active_type):
  active_type_counter = 0
  for row in range(start_row, finish_row + 1):
    if active_type == csv_data_list[row][2]:
      active_type_counter += 1
    else:
      continue
      
  return active_type_counter