import couple_csv_data_list
import think_range
import couple_think
couple_csv_data = couple_csv_data_list.couple_csv_data_list()

for file_path_count in range(couple_csv_data):
  numfour_csv_data = couple_csv_data[0][file_path_count]
  numfive_csv_data = couple_csv_data[1][file_path_count]
  
  #1 
  heart_suit_time = couple_think.couple_heart_suit_time(numfour_csv_data, numfive_csv_data)

  #2

  