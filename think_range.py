import thinks
import before_and_after_file_range_csv_list
# 心拍計測定開始位置から行動計装着開始時間を求める関数
def start_active_counter_row(csv_data):
  not_use = 0
  heart_start_row = thinks.return_heart_counter_start_row(csv_data)

  active_start_row = 0
  row_count = thinks.return_heart_counter_start_row([csv_data])
  for row in range(20):
    if float(csv_data[row_count][1]) != 0:
      active_start_row = row_count
    else:
       row_count = row_count - 1
    
  if active_start_row == 0:
    for row in range(heart_start_row, heart_start_row + 40): 
      if float(csv_data[row][1]) != 0:
        active_start_row = row
        break
  return active_start_row

def finish_active_counter_row(csv_data):
  row_count = thinks.return_heart_counter_finish_row(csv_data) 
  row_count_backup = row_count
  finish_active_count_row = 0
  for row in range(40):
    if float(csv_data[row_count][1]) != 0:
      finish_active_count_row = row_count
      break
    else:
      row_count = row_count - 1 
  
  row_count = row_count_backup
  for row in range(40):
    print(row_count)
    if float(csv_data[row_count][1]) != 0:
      finish_active_count_row = row_count
      row_count = row_count + 1
    else:
      row_count = row_count + 1
  return finish_active_count_row

# 心拍計測定位置など関係なく行動計装着時間を求める関数
def full_start_active_counter_row(csv_data):
  for row in range(len(csv_data)):
    if float(csv_data[row][1]) != 0:
     start_row = row
     break
    else:
      continue
  
  return start_row

def full_finish_active_counter_row(csv_data):
  last_row = len(csv_data) - 1
  for row in range(1444):
    if float(csv_data[last_row][1]) != 0:
      answer = last_row
      break
    else:
      last_row = last_row - 1
  return answer    

def before_csv_data_split(csv_data):
  for row in range(len(csv_data)):
    if csv_data[row][0] == '04:01:00':
      answer = row - 1
      break 
  if answer == -1:
    answer = 0 
  return answer      

def after_csv_data_split(csv_data):
  for row in range(len(csv_data)):
    if csv_data[row][0] == '23:59:00':
      answer = row
  return answer
  
