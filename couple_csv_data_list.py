import return_file_path
import return_file_csv_list
import pprint

def couple_csv_data_list():
  numfour_file_path = return_file_path.numfour_couple_data()
  numfive_file_path = return_file_path.numfive_couple_data()
  couple_csv_data_list = []
  numfour_csv_list = []
  numfive_csv_list = []

  for file_path in numfour_file_path:
    numfour_csv_data = return_file_csv_list.return_file_csv_data_list(file_path)
    numfour_csv_list.append(numfour_csv_data) 
  
  for file_path in numfive_file_path:
    numfive_csv_data = return_file_csv_list.return_file_csv_data_list(file_path)
    numfive_csv_list.append(numfive_csv_data)

  couple_csv_data_list.append(numfour_csv_list)
  couple_csv_data_list.append(numfive_csv_list)

  return couple_csv_data_list
