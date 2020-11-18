def add_time(start, duration, day = False):
    
    # Split the start time into two parts, the time and the half of the day
    start_list= start.split()
    start_time = start_list[0]

    # Convert the time to [time in minutes since 0:00]
    if start_list[1] == 'PM':
        hours_to_add = 12
    else:
        hours_to_add = 0
    s_hour = start_time.split(':')[0]
    s_time = start_time.split(':')[1]
    print(s_hour)
    print(s_time)

#    return new_time


add_time('3:00 PM', '3:00')
