def read_data(file_name):
    with open(file_name, encoding='utf-8') as f:
        reader = csv.reader(f)
        list = [row for row in reader]
        return list
def total_heart_rate_count(target_string, )
