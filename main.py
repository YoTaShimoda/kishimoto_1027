import before_and_after_file_range_csv_list
import think_range
import thinks
import csv
import return_file_path
import os

numfour_list = before_and_after_file_range_csv_list.numfour_before_and_after_file_range_csv_list()
numfive_list = before_and_after_file_range_csv_list.numfive_before_and_after_file_range_csv_list()
numfour_file_path = return_file_path.numfour_before_and_after_file()
numfive_file_path = return_file_path.numfive_before_ane_after_file()
answer =[] 
count = 0
for data_list in numfour_list:
   before_data_finish_row = think_range.before_csv_data_split(data_list)
   before_data = data_list[:before_data_finish_row] 
   after_data_finish_row = think_range.after_csv_data_split(data_list)
   after_data = data_list[before_data_finish_row : after_data_finish_row + 1]
#    # 行動計の範囲を変える時はここを変える
   try:   
      before_active_count_start_row = think_range.start_active_counter_row(before_data)
   except:
      before_active_count_start_row = 0
   try:
      before_active_count_finish_row = think_range.finish_active_counter_row(before_data)
   except:
      before_active_count_finish_row = 0

   after_active_count_start_row = think_range.start_active_counter_row(after_data)

   after_active_count_finish_row = think_range.finish_active_counter_row(after_data)

   # 1
   try:
      before_heart_count_suit_time = thinks.return_heart_counter_suit_time(before_data)
   except:
      before_heart_count_suit_time = 0

   after_heart_count_suit_time = thinks.return_heart_counter_suit_time(after_data)
   heart_count_suit_time = before_heart_count_suit_time + after_heart_count_suit_time 

   # 2
   try:
      before_acitve_count_suit_time = thinks.return_active_counter_suit_time(before_active_count_start_row, before_active_count_finish_row)  
   except:
      before_acitve_count_suit_time = 0
      
   after_active_count_suit_time = thinks.return_active_counter_suit_time(after_active_count_start_row, after_active_count_finish_row)
   active_counter_suit_time = before_acitve_count_suit_time + after_active_count_suit_time 
   
   # 3
   try:
      before_both_counter_suit_time = thinks.return_both_counter_suit_time(before_data, before_active_count_start_row, before_active_count_finish_row)
   except:
      before_both_counter_suit_time = 0

   after_both_counter_suit_time = thinks.return_both_counter_suit_time(after_data, after_active_count_start_row, after_active_count_finish_row)
   both_counter_suit_time = before_both_counter_suit_time + after_both_counter_suit_time 

   # 4
   try:
      before_life_type_active_counter = thinks.active_type_counter(before_data, before_active_count_start_row, after_active_count_finish_row, '生活活動')
   except:
      before_life_type_active_counter = 0

   after_life_type_active_counter = thinks.active_type_counter(after_data, after_active_count_start_row, after_active_count_finish_row, '生活活動') 
   life_type_active_counter = before_life_type_active_counter + after_life_type_active_counter 

   # 5
   try:
      before_walk_type_active_counter = thinks.active_type_counter(before_data, before_active_count_start_row, after_active_count_finish_row, '歩行')
   except:
      before_walk_type_active_counter = 0

   afterw_walk_type_active_counter = thinks.active_type_counter(after_data, after_active_count_start_row, after_active_count_finish_row, '歩行') 
   walk_type_active_counter = before_walk_type_active_counter + afterw_walk_type_active_counter 
   
   # 6
   try:
      before_not_active_counter = thinks.active_type_counter(before_data, before_active_count_start_row, before_active_count_finish_row, '計測なし')
   except:
      before_not_active_counter = 0
      
   after_not_active_counter = thinks.active_type_counter(after_data, after_active_count_start_row, after_active_count_finish_row, '計測なし')
   not_active_counter = before_not_active_counter + after_not_active_counter 
     
   # 7
   try:
      before_life_type_both_counter_suit_count = thinks.active_type_count_for_both_counter_suit(before_data, before_active_count_start_row, after_active_count_finish_row, '生活活動')   
   except:
      before_life_type_both_counter_suit_count = 0

   after_life_type_both_counter_suit_count = thinks.active_type_count_for_both_counter_suit(after_data, after_active_count_start_row, after_active_count_finish_row, '生活活動')
   life_type_both_counter_suit_count  = before_life_type_active_counter + after_life_type_both_counter_suit_count
   
   # 8
   try:
      before_walk_type_both_counter_suit_count = thinks.active_type_count_for_both_counter_suit(before_data, before_active_count_start_row, after_active_count_finish_row, '歩行')
   except:
      before_walk_type_both_counter_suit_count = 0

   after_walk_type_both_counter_suit_count = thinks.active_type_count_for_both_counter_suit(after_data, after_active_count_start_row, after_active_count_finish_row, '歩行')
   walk_type_both_counter_suit_count = before_walk_type_both_counter_suit_count + after_walk_type_both_counter_suit_count

   # 9
   try:
      before_not_active_both_counter_suit_count = thinks.active_type_count_for_both_counter_suit(before_data, before_active_count_start_row, before_active_count_finish_row, '計測なし')
   except:
      before_not_active_both_counter_suit_count = 0

   after_not_active_both_counter_suit_count = thinks.active_type_count_for_both_counter_suit(after_data, after_active_count_start_row, after_active_count_finish_row, '計測なし') 
   not_active_both_counter_suit_count = before_not_active_both_counter_suit_count + after_not_active_both_counter_suit_count

   # 10
   try:
      before_both_suit_mets_average = thinks.average_mets_count(before_data, before_active_count_start_row, before_active_count_finish_row)
   except:
      before_both_suit_mets_average = 0

   after_both_suit_mets_average = thinks.average_mets_count(after_data, after_active_count_start_row, after_active_count_finish_row)
   both_suit_count_mets_average = before_both_suit_mets_average + after_both_suit_mets_average
   if before_both_suit_mets_average == 0:
      both_suit_count_mets_average = both_suit_count_mets_average 
   else:
      both_suit_count_mets_average = both_suit_count_mets_average / 2

   # 11
   try:
      before_both_suit_heart_average = thinks.average_heart_count(before_data, before_active_count_start_row, before_active_count_finish_row)
   except:
      before_both_suit_heart_average = 0

   after_both_suit_heart_average = thinks.average_heart_count(after_data, after_active_count_start_row, after_active_count_finish_row)
   both_suit_heart_average = before_both_suit_heart_average + after_both_suit_heart_average
   if before_both_suit_heart_average == 0:
      both_suit_heart_average = both_suit_heart_average
   else:
      both_suit_heart_average = both_suit_heart_average / 2
   
   # 12
   try:
      before_life_type_heart_average = thinks.average_heart_count_for_active_type(before_data, before_active_count_start_row, after_active_count_finish_row, '生活活動')
   except:
      before_life_type_heart_average = 0

   after_life_type_heart_average = thinks.average_heart_count_for_active_type(after_data, after_active_count_start_row, after_active_count_finish_row, '生活活動') 
   life_type_heart_average = before_life_type_heart_average + after_life_type_heart_average
   if before_life_type_heart_average == 0:
      life_type_heart_average = life_type_heart_average
   else:
      life_type_heart_average = life_type_heart_average / 2

   # 13
   try:
      before_walk_type_heart_average = thinks.average_heart_count_for_active_type(before_data, before_active_count_start_row, after_active_count_finish_row, '歩行')
   except:
      before_walk_type_heart_average = 0

   after_walk_type_heart_average = thinks.average_heart_count_for_active_type(after_data, after_active_count_start_row, after_active_count_finish_row, '歩行')
   walk_type_heart_average = before_walk_type_heart_average + after_walk_type_heart_average
   if before_walk_type_heart_average == 0:
      walk_type_heart_average = walk_type_heart_average 
   else:
      walk_type_heart_average = walk_type_heart_average / 2

   # 14
   try:
      before_life_type_mets_average = thinks.average_mets_count_for_avtive_type(before_data, before_active_count_start_row, after_active_count_finish_row, '生活活動')
   except:
      before_life_type_mets_average = 0
      
   after_life_type_mets_average = thinks.average_mets_count_for_avtive_type(after_data, after_active_count_start_row, after_active_count_finish_row, '生活活動')
   life_type_mets_average = before_life_type_mets_average + after_life_type_mets_average
   if before_life_type_mets_average == 0:
      life_type_mets_average = life_type_mets_average
   else:
      life_type_mets_average = life_type_mets_average / 2
   
   # 15
   try:
      before_walk_type_mets_average = thinks.average_mets_count_for_avtive_type(before_data, before_active_count_start_row, after_active_count_finish_row, '歩行')
   except:
      before_walk_type_mets_average = 0

   after_walk_type_mets_average = thinks.average_mets_count_for_avtive_type(after_data, after_active_count_start_row, after_active_count_finish_row, '歩行') 
   walk_type_mets_average = before_walk_type_mets_average + after_walk_type_mets_average
   if before_walk_type_mets_average == 0:
      walk_type_mets_average = walk_type_mets_average
   else:
      walk_type_mets_average = walk_type_mets_average 
   
   # 16
   try:
      before_average_heart_count_for_not_active = thinks.average_heart_count_for_not_active(before_data)
   except:
      before_average_heart_count_for_not_active = 0

   after_average_heart_count_for_not_active = thinks.average_heart_count_for_not_active(after_data)
   average_heart_count_for_not_active = before_average_heart_count_for_not_active + after_average_heart_count_for_not_active
   if before_average_heart_count_for_not_active == 0:
      average_heart_count_for_not_active = average_heart_count_for_not_active 
   else:
      average_heart_count_for_not_active = average_heart_count_for_not_active

   # 17
   try:
      before_total_active_count = thinks.total_active_count(before_data)   
   except:
      before_total_active_count = 0
      
   after_total_active_count = thinks.total_active_count(after_data)
   total_active_count = before_total_active_count + after_total_active_count
   
   # 18
   try:
      before_both_counter_suit_total_active_count = thinks.both_counter_suit_total_active_count(before_data, before_active_count_start_row, before_active_count_finish_row)
   except:
      before_both_counter_suit_time = 0

   after_both_counter_suit_total_active_count = thinks.both_counter_suit_total_active_count(after_data, after_active_count_start_row, after_active_count_finish_row)
   both_counter_suit_total_active_count = before_both_counter_suit_time + after_both_counter_suit_time
   
   
   file_name = numfour_file_path[count]
   file_name = os.path.basename(file_name)

   numfour_answer = {'a':file_name, 'b':heart_count_suit_time, 'c':active_counter_suit_time, 'd':both_counter_suit_time, 'e':life_type_active_counter,
    'f':walk_type_active_counter, 'g':not_active_counter, 'h':life_type_both_counter_suit_count, 'i':walk_type_both_counter_suit_count, 
    'j':not_active_both_counter_suit_count, 'k':both_suit_count_mets_average, 'l':both_suit_heart_average, 'm':life_type_heart_average, 'o':walk_type_heart_average, 
    'p':life_type_mets_average, 'q':walk_type_mets_average, 'r':average_heart_count_for_not_active, 's':total_active_count, 't':both_counter_suit_total_active_count}
   
   numfour_answer = sorted(numfour_answer.items()) 
   answer_list = []
   for value in numfour_answer:
      answer_list.append(value[1])
   count += 1
   answer.append(answer_list)

   # break
with open('answer/no4_answer.csv', 'w', newline='') as f:
   writer = csv.writer(f)
   for row in answer:
      writer.writerow(row)

answer = []
count = 0
for data_list in numfive_list:
   before_data_finish_row = think_range.before_csv_data_split(data_list)
   before_data = data_list[:before_data_finish_row] 
   after_data_finish_row = think_range.after_csv_data_split(data_list)
   after_data = data_list[before_data_finish_row : after_data_finish_row + 1]
#    # 行動計の範囲を変える時はここを変える
   try:   
      before_active_count_start_row = think_range.start_active_counter_row(before_data)
   except:
      before_active_count_start_row = 0
   try:
      before_active_count_finish_row = think_range.finish_active_counter_row(before_data)
   except:
      before_active_count_finish_row = 0

   after_active_count_start_row = think_range.start_active_counter_row(after_data)

   after_active_count_finish_row = think_range.finish_active_counter_row(after_data)

   # 1
   try:
      before_heart_count_suit_time = thinks.return_heart_counter_suit_time(before_data)
   except:
      before_heart_count_suit_time = 0

   after_heart_count_suit_time = thinks.return_heart_counter_suit_time(after_data)
   heart_count_suit_time = before_heart_count_suit_time + after_heart_count_suit_time 

   # 2
   try:
      before_acitve_count_suit_time = thinks.return_active_counter_suit_time(before_active_count_start_row, before_active_count_finish_row)  
   except:
      before_acitve_count_suit_time = 0
      
   after_active_count_suit_time = thinks.return_active_counter_suit_time(after_active_count_start_row, after_active_count_finish_row)
   active_counter_suit_time = before_acitve_count_suit_time + after_active_count_suit_time 
   
   # 3
   try:
      before_both_counter_suit_time = thinks.return_both_counter_suit_time(before_data, before_active_count_start_row, before_active_count_finish_row)
   except:
      before_both_counter_suit_time = 0

   after_both_counter_suit_time = thinks.return_both_counter_suit_time(after_data, after_active_count_start_row, after_active_count_finish_row)
   both_counter_suit_time = before_both_counter_suit_time + after_both_counter_suit_time 

   # 4
   try:
      before_life_type_active_counter = thinks.active_type_counter(before_data, before_active_count_start_row, after_active_count_finish_row, '生活活動')
   except:
      before_life_type_active_counter = 0

   after_life_type_active_counter = thinks.active_type_counter(after_data, after_active_count_start_row, after_active_count_finish_row, '生活活動') 
   life_type_active_counter = before_life_type_active_counter + after_life_type_active_counter 

   # 5
   try:
      before_walk_type_active_counter = thinks.active_type_counter(before_data, before_active_count_start_row, after_active_count_finish_row, '歩行')
   except:
      before_walk_type_active_counter = 0

   afterw_walk_type_active_counter = thinks.active_type_counter(after_data, after_active_count_start_row, after_active_count_finish_row, '歩行') 
   walk_type_active_counter = before_walk_type_active_counter + afterw_walk_type_active_counter 
   
   # 6
   try:
      before_not_active_counter = thinks.active_type_counter(before_data, before_active_count_start_row, before_active_count_finish_row, '計測なし')
   except:
      before_not_active_counter = 0
      
   after_not_active_counter = thinks.active_type_counter(after_data, after_active_count_start_row, after_active_count_finish_row, '計測なし')
   not_active_counter = before_not_active_counter + after_not_active_counter 
     
   # 7
   try:
      before_life_type_both_counter_suit_count = thinks.active_type_count_for_both_counter_suit(before_data, before_active_count_start_row, after_active_count_finish_row, '生活活動')   
   except:
      before_life_type_both_counter_suit_count = 0

   after_life_type_both_counter_suit_count = thinks.active_type_count_for_both_counter_suit(after_data, after_active_count_start_row, after_active_count_finish_row, '生活活動')
   life_type_both_counter_suit_count  = before_life_type_active_counter + after_life_type_both_counter_suit_count
   
   # 8
   try:
      before_walk_type_both_counter_suit_count = thinks.active_type_count_for_both_counter_suit(before_data, before_active_count_start_row, after_active_count_finish_row, '歩行')
   except:
      before_walk_type_both_counter_suit_count = 0

   after_walk_type_both_counter_suit_count = thinks.active_type_count_for_both_counter_suit(after_data, after_active_count_start_row, after_active_count_finish_row, '歩行')
   walk_type_both_counter_suit_count = before_walk_type_both_counter_suit_count + after_walk_type_both_counter_suit_count

   # 9
   try:
      before_not_active_both_counter_suit_count = thinks.active_type_count_for_both_counter_suit(before_data, before_active_count_start_row, before_active_count_finish_row, '計測なし')
   except:
      before_not_active_both_counter_suit_count = 0

   after_not_active_both_counter_suit_count = thinks.active_type_count_for_both_counter_suit(after_data, after_active_count_start_row, after_active_count_finish_row, '計測なし') 
   not_active_both_counter_suit_count = before_not_active_both_counter_suit_count + after_not_active_both_counter_suit_count

   # 10
   try:
      before_both_suit_mets_average = thinks.average_mets_count(before_data, before_active_count_start_row, before_active_count_finish_row)
   except:
      before_both_suit_mets_average = 0

   after_both_suit_mets_average = thinks.average_mets_count(after_data, after_active_count_start_row, after_active_count_finish_row)
   both_suit_count_mets_average = before_both_suit_mets_average + after_both_suit_mets_average
   if before_both_suit_mets_average == 0:
      both_suit_count_mets_average = both_suit_count_mets_average 
   else:
      both_suit_count_mets_average = both_suit_count_mets_average / 2

   # 11
   try:
      before_both_suit_heart_average = thinks.average_heart_count(before_data, before_active_count_start_row, before_active_count_finish_row)
   except:
      before_both_suit_heart_average = 0

   after_both_suit_heart_average = thinks.average_heart_count(after_data, after_active_count_start_row, after_active_count_finish_row)
   both_suit_heart_average = before_both_suit_heart_average + after_both_suit_heart_average
   if before_both_suit_heart_average == 0:
      both_suit_heart_average = both_suit_heart_average
   else:
      both_suit_heart_average = both_suit_heart_average / 2
   
   # 12
   try:
      before_life_type_heart_average = thinks.average_heart_count_for_active_type(before_data, before_active_count_start_row, after_active_count_finish_row, '生活活動')
   except:
      before_life_type_heart_average = 0

   after_life_type_heart_average = thinks.average_heart_count_for_active_type(after_data, after_active_count_start_row, after_active_count_finish_row, '生活活動') 
   life_type_heart_average = before_life_type_heart_average + after_life_type_heart_average
   if before_life_type_heart_average == 0:
      life_type_heart_average = life_type_heart_average
   else:
      life_type_heart_average = life_type_heart_average / 2

   # 13
   try:
      before_walk_type_heart_average = thinks.average_heart_count_for_active_type(before_data, before_active_count_start_row, after_active_count_finish_row, '歩行')
   except:
      before_walk_type_heart_average = 0

   after_walk_type_heart_average = thinks.average_heart_count_for_active_type(after_data, after_active_count_start_row, after_active_count_finish_row, '歩行')
   walk_type_heart_average = before_walk_type_heart_average + after_walk_type_heart_average
   if before_walk_type_heart_average == 0:
      walk_type_heart_average = walk_type_heart_average 
   else:
      walk_type_heart_average = walk_type_heart_average / 2

   # 14
   try:
      before_life_type_mets_average = thinks.average_mets_count_for_avtive_type(before_data, before_active_count_start_row, after_active_count_finish_row, '生活活動')
   except:
      before_life_type_mets_average = 0
      
   after_life_type_mets_average = thinks.average_mets_count_for_avtive_type(after_data, after_active_count_start_row, after_active_count_finish_row, '生活活動')
   life_type_mets_average = before_life_type_mets_average + after_life_type_mets_average
   if before_life_type_mets_average == 0:
      life_type_mets_average = life_type_mets_average
   else:
      life_type_mets_average = life_type_mets_average / 2
   
   # 15
   try:
      before_walk_type_mets_average = thinks.average_mets_count_for_avtive_type(before_data, before_active_count_start_row, after_active_count_finish_row, '歩行')
   except:
      before_walk_type_mets_average = 0

   after_walk_type_mets_average = thinks.average_mets_count_for_avtive_type(after_data, after_active_count_start_row, after_active_count_finish_row, '歩行') 
   walk_type_mets_average = before_walk_type_mets_average + after_walk_type_mets_average
   if before_walk_type_mets_average == 0:
      walk_type_mets_average = walk_type_mets_average
   else:
      walk_type_mets_average = walk_type_mets_average 
   
   # 16
   try:
      before_average_heart_count_for_not_active = thinks.average_heart_count_for_not_active(before_data)
   except:
      before_average_heart_count_for_not_active = 0

   after_average_heart_count_for_not_active = thinks.average_heart_count_for_not_active(after_data)
   average_heart_count_for_not_active = before_average_heart_count_for_not_active + after_average_heart_count_for_not_active
   if before_average_heart_count_for_not_active == 0:
      average_heart_count_for_not_active = average_heart_count_for_not_active 
   else:
      average_heart_count_for_not_active = average_heart_count_for_not_active

   # 17
   try:
      before_total_active_count = thinks.total_active_count(before_data)   
   except:
      before_total_active_count = 0
      
   after_total_active_count = thinks.total_active_count(after_data)
   total_active_count = before_total_active_count + after_total_active_count
   
   # 18
   try:
      before_both_counter_suit_total_active_count = thinks.both_counter_suit_total_active_count(before_data, before_active_count_start_row, before_active_count_finish_row)
   except:
      before_both_counter_suit_time = 0

   after_both_counter_suit_total_active_count = thinks.both_counter_suit_total_active_count(after_data, after_active_count_start_row, after_active_count_finish_row)
   both_counter_suit_total_active_count = before_both_counter_suit_time + after_both_counter_suit_time

   file_name = numfive_file_path[count]
   file_name = os.path.basename(file_name)
   numfive_answer = {'a':file_name, 'b':heart_count_suit_time, 'c':active_counter_suit_time, 'd':both_counter_suit_time, 'e':life_type_active_counter,
    'f':walk_type_active_counter, 'g':not_active_counter, 'h':life_type_both_counter_suit_count, 'i':walk_type_both_counter_suit_count, 
    'j':not_active_both_counter_suit_count, 'k':both_suit_count_mets_average, 'l':both_suit_heart_average, 'm':life_type_heart_average, 'o':walk_type_heart_average, 
    'p':life_type_mets_average, 'q':walk_type_mets_average, 'r':average_heart_count_for_not_active, 's':total_active_count, 't':both_counter_suit_total_active_count}
   numfive_answer = sorted(numfive_answer.items()) 
   answer_list = []
   for value in numfive_answer:
      answer_list.append(value[1])
   count += 1
   answer.append(answer_list)

   # break
with open('answer/no5_answer.csv', 'w', newline='') as f:
   writer = csv.writer(f)
   for row in answer:
      writer.writerow(row)