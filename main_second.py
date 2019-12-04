import return_file_csv_list
import return_file_path
import think_second
import os
import csv

answer = []
for file_path in range(len(return_file_path.numfour_active())):
  numfour_heart_data = return_file_csv_list.heart_data(return_file_path.numfour_heart()[file_path])
  numfour_active_data = return_file_csv_list.return_file_csv_data_list(return_file_path.numfour_active()[file_path])
  count = 0

  # 1
  heart_suit_time = len(think_second.heart_suit_time(numfour_heart_data))

  # 2 
  active_suit_time = len(think_second.active_suit_time(numfour_active_data))

  # 3
  both_suit_time = len(think_second.both_suit_time(think_second.heart_suit_time(numfour_heart_data), think_second.active_suit_time(numfour_active_data)))

  # 4
  life_time_active = think_second.active_type_time(numfour_active_data, '生活活動')

  # 5
  walk_time_active = think_second.active_type_time(numfour_active_data, '歩行') 
  
  # 6
  noactive_time_active = think_second.active_type_time(numfour_active_data, '計測なし')

  # 7
  both_life = think_second.both_suit_type(numfour_heart_data, numfour_active_data, '生活活動')

  # 8
  both_walk = think_second.both_suit_type(numfour_heart_data, numfour_active_data, '歩行')

  # 9 
  both_no = think_second.both_suit_type(numfour_heart_data, numfour_active_data, '計測なし')

  # 10
  both_met_average = think_second.both_met_average(numfour_heart_data, numfour_active_data)

  # 11
  both_heart_average = think_second.both_heart_average(numfour_heart_data, numfour_active_data)

  # 12
  both_heart_average_life = think_second.both_heart_average_type(numfour_heart_data, numfour_active_data, '生活活動')

  # 13
  both_heart_average_walk = think_second.both_heart_average_type(numfour_heart_data, numfour_active_data, '歩行')
  
  # 14
  both_met_average_life = think_second.both_met_average_type(numfour_heart_data, numfour_active_data, '生活活動')

  # 15
  both_met_average_walk = think_second.both_met_average_type(numfour_heart_data, numfour_active_data, '歩行')
  
  # 16
  not_count_heart_average = think_second.both_heart_average_type(numfour_heart_data, numfour_active_data, '計測なし')

  # 17
  total_mets = think_second.total_mets(numfour_active_data)

  # 18
  both_total_mets = think_second.both_mets_total(numfour_heart_data, numfour_active_data)

  file_path = return_file_path.numfour_heart()[file_path]
  file_name = file_path
  print(file_name)
  file_name = os.path.basename(file_name)
  answer_list = []
  numfive_answer = {'a':file_name, 'b':heart_suit_time, 'c':active_suit_time, 'd':both_suit_time, 'e':life_time_active,
  'f':walk_time_active, 'g':noactive_time_active, 'h':both_life, 'i':both_walk, 
  'j':both_no, 'k':both_met_average, 'l':both_heart_average, 'm':both_heart_average_life, 'o':both_heart_average_walk, 
  'p':both_met_average_life, 'q':both_met_average_walk, 'r':not_count_heart_average, 's':total_mets, 't':both_total_mets}
  numfive_answer = sorted(numfive_answer.items()) 
  for value in numfive_answer:
    answer_list.append(value[1])
  count += 1
  answer.append(answer_list)

with open('answer_2/no4/' + file_name, 'w', newline='') as f:
   writer = csv.writer(f)
   for row in answer:
      writer.writerow(row)

for file_path in range(len(return_file_path.numfive_active())):
  numfive_heart_data = return_file_csv_list.heart_data(return_file_path.numfive_heart()[file_path])
  numfive_active_data = return_file_csv_list.return_file_csv_data_list(return_file_path.numfive_active()[file_path])
  count = 0

  # 1
  heart_suit_time = len(think_second.heart_suit_time(numfive_heart_data))

  # 2 
  active_suit_time = len(think_second.active_suit_time(numfive_active_data))

  # 3
  both_suit_time = len(think_second.both_suit_time(think_second.heart_suit_time(numfive_heart_data), think_second.active_suit_time(numfive_active_data)))

  # 4
  life_time_active = think_second.active_type_time(numfive_active_data, '生活活動')

  # 5
  walk_time_active = think_second.active_type_time(numfive_active_data, '歩行') 
  
  # 6
  noactive_time_active = think_second.active_type_time(numfive_active_data, '計測なし')

  # 7
  both_life = think_second.both_suit_type(numfive_heart_data, numfive_active_data, '生活活動')

  # 8
  both_walk = think_second.both_suit_type(numfive_heart_data, numfive_active_data, '歩行')

  # 9 
  both_no = think_second.both_suit_type(numfive_heart_data, numfive_active_data, '計測なし')

  # 10
  both_met_average = think_second.both_met_average(numfive_heart_data, numfive_active_data)

  # 11
  both_heart_average = think_second.both_heart_average(numfive_heart_data, numfive_active_data)

  # 12
  both_heart_average_life = think_second.both_heart_average_type(numfive_heart_data, numfive_active_data, '生活活動')

  # 13
  both_heart_average_walk = think_second.both_heart_average_type(numfive_heart_data, numfive_active_data, '歩行')
  
  # 14
  both_met_average_life = think_second.both_met_average_type(numfive_heart_data, numfive_active_data, '生活活動')

  # 15
  both_met_average_walk = think_second.both_met_average_type(numfive_heart_data, numfive_active_data, '歩行')
  
  # 16
  not_count_heart_average = think_second.both_heart_average_type(numfive_heart_data, numfive_active_data, '計測なし')

  # 17
  total_mets = think_second.total_mets(numfive_active_data)

  # 18
  both_total_mets = think_second.both_mets_total(numfive_heart_data, numfive_active_data)
  

  file_path = return_file_path.numfive_heart()[file_path]
  file_name = file_path
  file_name = os.path.basename(file_name)
  answer_list = []
  numfive_answer = {'a':file_name, 'b':heart_suit_time, 'c':active_suit_time, 'd':both_suit_time, 'e':life_time_active,
  'f':walk_time_active, 'g':noactive_time_active, 'h':both_life, 'i':both_walk, 
  'j':both_no, 'k':both_met_average, 'l':both_heart_average, 'm':both_heart_average_life, 'o':both_heart_average_walk, 
  'p':both_met_average_life, 'q':both_met_average_walk, 'r':not_count_heart_average, 's':total_mets, 't':both_total_mets}
  numfive_answer = sorted(numfive_answer.items()) 
  for value in numfive_answer:
    answer_list.append(value[1])
  count += 1
  answer.append(answer_list)
  print(file_name)

with open('answer_2/no5/' + file_name, 'w', newline='') as f:
   writer = csv.writer(f)
   for row in answer:
      writer.writerow(row)