import before_and_after_file_range_csv_list
import think_range
import thinks

numfour_list = before_and_after_file_range_csv_list.numfour_before_and_after_file_range_csv_list()
numfive_list = before_and_after_file_range_csv_list.numfive_before_and_after_file_range_csv_list()

for data_list in numfour_list:
   before_data_finish_row = think_range.before_csv_data_split(data_list)
   before_data = data_list[:before_data_finish_row] 
   after_data_finish_row = think_range.after_csv_data_split(data_list)
   after_data = data_list[before_data_finish_row : after_data_finish_row + 1]

   before_active_count_start_row = 0
   before_active_count_finish_row = 0
   after_active_count_finish_row = 0
   after_active_count_start_row = 0
   
   # 行動計の範囲を変える時はここを変える
   try:   
      before_active_count_start_row = think_range.start_active_counter_row(before_data)
      before_active_count_finish_row = think_range.finish_active_counter_row(before_data)
   except:
      before_active_count_start_row = []
      before_active_count_finish_row =[]
   try:
      after_active_count_start_row = think_range.start_active_counter_row(after_data)
      after_active_count_finish_row = think_range.finish_active_counter_row(after_data)
   except:
     after_active_count_start_row = []
     after_active_count_finish_row =[]

   #######################################  

   # 1
   before_heart_count_suit_time = thinks.return_heart_counter_suit_time(before_data)
   after_heart_count_suit_time = thinks.return_heart_counter_suit_time(after_data)
   heart_count_suit_time = before_heart_count_suit_time + after_heart_count_suit_time
   
   # 2
   try:
      before_active_counter_suit_time = thinks.return_active_counter_suit_time()
   except:
      before_active_count_suit_time = 0

    
   

   










   
# numfour_range = think_range.before_csv_data_split(numfour_list[0])
# answer = numfour_list[0][:numfour_range]
# numfour_finish = think_range.after_csv_data_split(numfour_list[0])
# numfour_after_range = numfour_list[0][numfour_range - 1:numfour_finish + 1]
# print(numfour_after_range)