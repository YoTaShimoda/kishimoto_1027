import return_file_path

def read_data(file_name):
    with open(file_name, encoding='utf-8') as f:
        reader = csv.reader(f)
        list = [row for row in reader]
        return list

class Main:    
    file_path = return_file_path
        
