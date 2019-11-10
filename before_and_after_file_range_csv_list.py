import return_file_csv_list
import return_file_path

def numfour_before_and_after_file_range_csv_list():
  numfour_file_path_list = return_file_path.numfour_return_file_path()
  main_data_list_numfour = [] 
  main_list = [] 
  for counter in range(len(numfour_file_path_list)):
    try:
      before_file_path = numfour_file_path_list[counter - 1]
    except:
      before_file_path = []
      continue

    after_file_path = numfour_file_path_list[counter]

    try:
      before_file_path_csv_data = return_file_csv_list.return_file_csv_data_list(before_file_path)
    except:
      before_file_path_csv_data = []

    try:
      before_file_path_csv_data = before_file_path_csv_data[1444:1685]
    except:
      continue

    after_file_path_csv_data = return_file_csv_list.return_file_csv_data_list(after_file_path)
    after_file_path_csv_data = after_file_path_csv_data[245:1444]
    main_data_list_numfour = before_file_path_csv_data
    for row in range(len(after_file_path_csv_data)):
      append_data = after_file_path_csv_data[row]
      main_data_list_numfour.append(append_data) 
    main_list.append(main_data_list_numfour)
  return main_list    

def numfive_before_and_after_file_range_csv_list():
  numfive_file_path_list = return_file_path.numfive_return_file_path()
  main_data_list_numfive = []
  main_list = []
  for counter in range(len(numfive_file_path_list)): 
    try:
      before_file_path = numfive_file_path_list[counter - 1]
    except:
      before_file_path = []
      continue
      
    after_file_path = numfive_file_path_list[counter]

    try:
      before_file_path_csv_data = return_file_csv_list.return_file_csv_data_list(before_file_path)
    except:
      before_file_path_csv_data = []

    try:
      before_file_path_csv_data = before_file_path_csv_data[1444:1685]
    except:
      continue

    after_file_path_csv_data = return_file_csv_list.return_file_csv_data_list(after_file_path)
    after_file_path_csv_data = after_file_path_csv_data[245:1444]
    main_data_list_numfive = before_file_path_csv_data
    for row in range(len(after_file_path_csv_data)):
      append_data = after_file_path_csv_data[row]
      main_data_list_numfive.append(append_data)
    main_list.append(main_data_list_numfive)
  return main_list 
