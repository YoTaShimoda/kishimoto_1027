import csv

def return_file_csv_data_list(file_path):
  with open(file_path, encoding='utf-8') as f:
    reader = csv.reader(f)
    list = [row for row in reader]  # リスト型に変換している
  return list   

def heart_data(file_path):
  csv_data = return_file_csv_data_list(file_path)
  return csv_data[4:]
   
        
        