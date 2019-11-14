import before_and_after_file_range_csv_list
import think_range
import thinks
import pprint
import datetime
import csv
import os
import return_file_path

numfour_list = before_and_after_file_range_csv_list.numfour_before_and_after_file_range_csv_list()
numfive_list = before_and_after_file_range_csv_list.numfive_before_and_after_file_range_csv_list()
answer = []


numfour_file_path = return_file_path.numfour_return_file_path()
numfive_file_path = return_file_path.numfive_return_file_path()
numfour_file_names = []
numfive_file_names = []

for file_path in numfour_file_path:
  base_name = os.path.basename(file_path)
  numfour_file_names.append(base_name)

for file_path in numfive_file_path:
  base_name = os.path.basename(file_path)
  numfive_file_names.append(base_name)

for data_list in range(len(numfour_list)):
   before_data_finish_row = think_range.before_csv_data_split(numfour_list[data_list])
   before_data = numfour_list[data_list][:before_data_finish_row] 
   after_data_finish_row = think_range.after_csv_data_split(numfour_list[data_list])
   after_data = numfour_list[data_list][before_data_finish_row : after_data_finish_row + 1]

   file_name = numfour_file_names[data_list]

   with open('test_csv_files/no4/' + file_name + '.csv', 'w') as f:
      writer = csv.writer(f)
      writer.writerows(before_data)
      writer.writerows(after_data) 
   

for data_list in range(len(numfive_list)):
   before_data_finish_row = think_range.before_csv_data_split(numfive_list[data_list])
   before_data = numfive_list[data_list][:before_data_finish_row] 
   after_data_finish_row = think_range.after_csv_data_split(numfive_list[data_list])
   after_data = numfive_list[data_list][before_data_finish_row : after_data_finish_row + 1]

   file_name = numfive_file_names[data_list]

   with open('test_csv_files/no5/' + file_name + '.csv', 'w') as f:
      writer = csv.writer(f)
      writer.writerows(before_data)
      writer.writerows(after_data) 
   