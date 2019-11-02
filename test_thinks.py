import return_file_csv_list
import thinks

file_path = 'test.csv'
print('start_rowを入力')
start_row = int(input()) - 1
print('finish_rowを入力')
finish_row = int(input()) - 1
csv_data_list = return_file_csv_list.return_file_csv_data_list(file_path)

def test_return_heart_counter_suit_time(csv_data_list):
  answer = thinks.return_heart_counter_suit_time(csv_data_list)
  print(answer)

def test_return_active_counter_suit_time(start_row, finish_row):
  answer = thinks.return_active_counter_suit_time(start_row, finish_row)
#  print(answer)

def test_return_both_counter_suit_time(csv_data_list, start_row, finish_row):
  answer = thinks.return_both_counter_suit_time(csv_data_list, start_row, finish_row)
  print(answer)

def test_return_active_life_counter(csv_data_list, start_row, finish_row):
  answer = thinks.return_active_type_counter(csv_data_list, start_row, finish_row, '生活活動')
  print(answer)

'''
def test_return_heart_counter_start_row(csv_data_list):
  answer = thinks.return_heart_counter_start_row(csv_data_list)
  answer2 = thinks.return_heart_counter_finish_row(csv_data_list)
  print(answer)
  print(answer2)
'''

test_return_heart_counter_suit_time(csv_data_list)
test_return_active_counter_suit_time(start_row, finish_row)
test_return_both_counter_suit_time(csv_data_list, start_row, finish_row)
test_return_active_life_counter(csv_data_list, start_row, finish_row)
# test_return_heart_counter_start_row(csv_data_list)