import thinks
import couple_csv_data_list
import think_range

numfour_test = couple_csv_data_list.couple_csv_data_list()[0][1]
numfive_test = couple_csv_data_list.couple_csv_data_list()[1][1]

def couple_heart_suit_time(numfour, numfive):
  hako = 0
  heart_suit_row = []
  for row in range(len(numfour_test)):
    try:
      hako = numfour[row][3]
      hako = numfive[row][3]
      heart_suit_row.append(row)
    except:
      continue
  
  return heart_suit_row
