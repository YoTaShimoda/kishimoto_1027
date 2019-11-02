import return_file_path
import return_file_csv_list

for numfour_file_path in return_file_path.numfour_return_file_path():
# ここに取得するセルを判断するメソッドを書いていく
   print(numfour_file_path + 'のスタートrowを入力')
   active_counter_start_row = input()
   print(numfour_file_path + 'のフィニッシュrowを入力')
   active_counter_finish_row = input()
   csv_data_list = return_file_csv_list.return_file_csv_data_list(numfour_file_path)

for numfive_file_path in return_file_path.numfive_return_file_path():
# ここに取得するセルを判断するメソッドを書いていく
   csv_data_list = return_file_csv_list.return_file_csv_data_list(numfive_file_path)
   print(numfive_file_path + 'のスタートrowを入力')
   active_suit_couter_start_row = input()
   print(numfive_file_path + 'のフィニッシュrowを入力')
   active_counter_finish_row = input()

