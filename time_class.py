def count_time(start_time, finish_time):
    start_time_minute = start_time[3:5]
    finish_time_minute = finish_time[3:5]
    answer_time_minute = int(finish_time_minute) - int(start_time_minute)
    start_time_hour = start_time[:2]
    finish_time_hour = finish_time[:2]
    answer_time_hour = int(finish_time_hour) - int(start_time_hour)
    
    if answer_time_minute < 0:
        answer_time_hour = answer_time_hour - 1
        answer_time_minute = 60 + answer_time_minute
        
    answer_time_hour_str = "0"+str(answer_time_hour) if answer_time_hour < 10 else str(answer_time_hour)
    answer_time_minute_str = "0" + str(answer_time_minute) if answer_time_minute < 10 else str(answer_time_minute)

    answer = answer_time_hour_str + ':' + answer_time_minute_str
    return answer
