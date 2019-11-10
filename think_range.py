import return_file_csv_list
import before_and_after_file_range_csv_list
import pprint
# 心拍計測定開始位置から行動計装着開始時間を求める関数
def start_active_counter_row(csv_data):
  not_use = 0
  for row in range(len(csv_data)):
    try:
     not_use = csv_data[row][3] 
     heart_start_row = row
     break
    except:
      continue
  active_start_row = 0
  row_count = 0
  for row in range(heart_start_row, heart_start_row + 20):
    if float(csv_data[row_count][1]) != 0:
      active_start_row = row
    else:
       row_count = row_count - 1
    
  if active_start_row == 0:
    for row in range(heart_start_row, heart_start_row + 40): 
      if float(csv_data[row][1]) != 0:
        active_start_row = row
        break
  return active_start_row

csv_data = before_and_after_file_range_csv_list.numfour_before_and_after_file_range_csv_list()
csv_data = csv_data[0]
start_row = start_active_counter_row(csv_data)
print(csv_data[start_row])
