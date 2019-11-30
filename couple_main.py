import couple_think
import return_file_path
import return_file_csv_list
import os
import csv

for file_path in range(len(return_file_path.numfour_active())):
  numfour_heart_data = return_file_csv_list.heart_data(return_file_path.numfour_heart())
  numfour_active_data = return_file_csv_list.return_file_csv_data_list(return_file_path.numfour_active())
  numfive_heart_data = return_file_csv_list.heart_data(return_file_path.numfive_heart())
  numfive_active_data = return_file_csv_list.return_file_csv_data_list(return_file_path.numfive_active())
  count = 0
  answer = []

  # 1
  heart_suit_time = len(couple_think.heart_suit_time(numfour_heart_data, numfive_heart_data))

  # 2 
  active_suit_time = len(couple_think.active_suit_time(numfour_active_data, numfive_active_data))

  # 3
  both_suit_time = len(couple_think.heart_suit_time(numfour_heart_data, numfive_heart_data), couple_think.active_suit_time(numfour_active_data, numfive_active_data))

  # 4
  life_time_active = couple_think.active_type_time(numfour_active_data, numfive_active_data, '生活活動')

  # 5
  walk_time_active = couple_think.active_type_time(numfour_active_data, numfive_active_data, '歩行') 
  
  # 6
  noactive_time_active = couple_think.active_type_time(numfour_active_data, numfive_active_data, '計測なし')

  # 7
  both_life = couple_think.both_suit_type(numfour_heart_data, numfour_active_data, numfive_heart_data, numfive_active_data, '生活活動')

  # 8
  both_walk = couple_think.both_suit_type(numfour_heart_data, numfour_active_data, numfive_heart_data, numfive_active_data, '歩行')

  # 9 
  both_no = couple_think.both_suit_type(numfour_heart_data, numfour_active_data, numfive_heart_data, numfive_active_data, '計測なし')

  # 10
  both_met_average = couple_think.both_met_average(numfour_heart_data, numfour_active_data, numfive_heart_data, numfive_active_data)

  # 11
  both_heart_average = couple_think.both_heart_average(numfour_heart_data, numfour_active_data, numfive_heart_data, numfive_active_data)

  # 12
  both_heart_average_life = couple_think.both_heart_average_type(numfour_heart_data, numfour_active_data, numfive_heart_data, numfive_active_data, '生活活動')

  # 13
  both_heart_average_walk = couple_think.both_heart_average_type(numfour_heart_data, numfour_active_data, numfive_heart_data, numfive_active_data, '歩行')
  
  # 14
  both_met_average_life = couple_think.both_met_average_type(numfour_heart_data, numfour_active_data, numfive_heart_data, numfive_active_data, '生活活動')

  # 15
  both_met_average_walk = couple_think.both_met_average_type(numfour_heart_data, numfour_active_data, numfive_heart_data, numfive_active_data, '歩行')
  
  # 16
  not_count_heart_average = couple_think.both_heart_average_type(numfour_heart_data, numfour_active_data, numfive_heart_data, numfive_active_data, '計測なし')

  # 17
  total_mets = couple_think.total_mets(numfour_active_data, numfive_active_data)

  # 18
  both_total_mets = couple_think.both_mets_total(numfour_heart_data, numfour_active_data, numfive_heart_data, numfive_active_data)
  

  file_name = file_path
  file_name = os.path.basename(file_name)
  numfive_answer = {'a':file_name, 'b':heart_suit_time, 'c':active_suit_time, 'd':both_suit_time, 'e':life_time_active,
  'f':walk_time_active, 'g':noactive_time_active, 'h':both_life, 'i':both_walk, 
  'j':both_no, 'k':both_met_average, 'l':both_heart_average, 'm':both_heart_average_life, 'o':both_heart_average_walk, 
  'p':both_met_average_life, 'q':both_met_average_walk, 'r':not_count_heart_average, 's':total_mets, 't':both_total_mets}
  numfive_answer = sorted(numfive_answer.items()) 
  answer_list = []
  for value in numfive_answer:
    answer_list.append(value[1])
  count += 1
  answer.append(answer_list)

with open('couple_answer/', 'w', newline='') as f:
   writer = csv.writer(f)
   for row in answer:
      writer.writerow(row)
