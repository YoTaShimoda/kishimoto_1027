import return_file_csv_list
import thinks

file_path = 'test.csv'
print('start_rowを入力')
start_row = int(input()) - 1
print('finish_rowを入力')
finish_row = int(input()) - 1
csv_data_list = return_file_csv_list.return_file_csv_data_list(file_path)

print(thinks.return_heart_counter_suit_time(csv_data_list))
print(thinks.return_active_counter_suit_time(start_row, finish_row))
print(thinks.return_both_counter_suit_time(csv_data_list, start_row, finish_row))
print(thinks.active_type_counter(csv_data_list, start_row, finish_row, '生活活動'))
print(thinks.active_type_count_for_both_counter_suit(csv_data_list, start_row, finish_row, '生活活動'))
print(thinks.average_mets_count(csv_data_list, start_row, finish_row))
print(thinks.average_heart_count(csv_data_list, start_row, finish_row))
print(thinks.average_heart_count_for_active_type(csv_data_list, start_row, finish_row, '生活活動'))
print(thinks.average_mets_count_for_avtive_type(csv_data_list, start_row, finish_row, '生活活動'))
print(thinks.average_heart_count_for_not_active(csv_data_list))
print(thinks.total_active_count(csv_data_list))
print(thinks.both_counter_suit_total_active_count(csv_data_list, start_row, finish_row))