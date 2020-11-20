def add_time(start, duration, day = False):
    
    # Split the start time into two parts, the time and the half of the day
    start_list= start.split()
    start_time = start_list[0]

    # Convert the start time to [time in minutes since 0:00]
    if start_list[1] == 'PM':
        hours_to_add = 12
    else:
        hours_to_add = 0
    s_hour = start_time.split(':')[0]
    s_minutes = start_time.split(':')[1]
    print(s_hour)
    print(s_minutes)
    
    s_hour = int((int(s_hour) + hours_to_add) * 60)
    s_total = int(s_minutes) + s_hour


    # Check if the duration is longer than 1 day

    # Split the duration string into its parts 
    d_hour = duration.split(':')[0]
    d_minutes = duration.split(':')[0]
    
    
    # Convert the strings to ints
    d_hour = int(d_hour)
    d_mins = int(d_minutes)


    # Convert duration to minutes
    d_hour_mins = int(d_hour) * 60
    d_time = int(d_mins) + d_hour_mins
    print('d_hour_mins = ' + str(d_hour_mins)) 
    print('d_time / (24*60) = ' + str(d_time/(24*60)))
    print(24*60)
    if d_time/(24*60) >= 1:
        print('duration is longer than a day')
        longer_than_day = True
    else:
        print('duration is not longer than a day')
        longer_than_day = False

    total_mins = s_total + d_time
    end_time_combi = total_mins / 60

    print(end_time_combi)
    

    if longer_than_day:
        day = 1
    else:
        day = 0
    while end_time_combi > 24:
        end_time_combi -= 24
        day += 1
    
    end_time_hrs = str(end_time_combi).split('.')
    end_time_hrs = end_time_hrs[0]
    end_time_mins = str(end_time_combi).split('.')
    end_time_mins = int(end_time_mins[1]) * 60
    if day > 1:
        new_time  = '{}:{} ({} days later)'.format(end_time_hrs, str(end_time_mins)[0:2], day)
    elif day == 0:
        new_time = '{}:{}'.format(end_time_hrs, str(end_time_mins)[0:2])
    elif day == 1:
        new_time = '{}:{} (next day)'.format(end_time_hrs, str(end_time_mins)[0:2]) 
   

    print(new_time)



#    return new_time


add_time('3:00 PM', '4:00')
