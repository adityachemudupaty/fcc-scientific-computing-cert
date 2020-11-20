def add_time(start, duration, day = False):
    


    # define day dictionaries
    day_dict = {'1': 'sunday', '2': 'monday', '3': 'tuesday', '4': 'wednesday', '5': 'thursday', '6': 'friday', '7': 'saturday'}

    day_dict_2 = {'sunday': '1', 'monday': '2', 'tuesday': '3', 'wednesday': '4', 'thursday': '5', 'friday': '6', 'saturday': '7'}

    # Split start time into two parts

    start_list = start.split()
    start_time = start_list[0]

    # Split time into hours and minutes 
    if start_list[1] == 'PM':
        hours_to_add = 12
    else:
        hours_to_add = 0

    start_hour = start_time.split(':')[0]
    start_minutes = start_time.split(':')[1]

    # Convert time into military time

    start_hour = int(start_hour) + hours_to_add
    start_minutes = int(start_minutes)

    d_hour = duration.split(':')[0]
    d_minutes = duration.split(':')[1]

    d_hour = int(d_hour)
    d_minutes = int(d_minutes)
    

    # Add times together

    final_hours = d_hour + start_hour
    final_minutes = d_minutes + start_minutes
    

    # Account for duration causing days to change
 
    minutes_carry = 0
    new_final_minutes = final_minutes
    if new_final_minutes >= 60:
        final_minutes = new_final_minutes % 60
        minutes_carry = new_final_minutes // 60 


    hours_carry = 0
    new_final_hours = final_hours + minutes_carry
    if final_hours >= 24:
        new_final_hours = new_final_hours % 24
        hours_carry = final_hours // 24


    # Write ending string
    if hours_carry == 1:
        end_string = '(next day)'
    elif hours_carry >= 2:
        end_string = '({} days later)'.format(hours_carry)
    else:
        end_string = ''

    if new_final_hours > 12:
        PM = 'PM' 
        new_final_hours = new_final_hours % 12
    else:
        PM = 'AM' 

    new_time = '{}:{}'.format(new_final_hours, str(final_minutes).zfill(2)) + ' ' + PM 


    if day != False:
        day = day.lower()
        new_time = new_time + ','
        day_num = day_dict_2[day] 
        day_num = int(day_num) + hours_carry
        final_day = day_dict[str(day_num % 7)]
    else:
        final_day = ''



    final_string = new_time + ' ' + end_string

    new_time = new_time + ' ' + final_day.title() + ' ' + end_string
    print(new_time)
    return(new_time)

add_time('3:00 PM', '3:10')
add_time("11:30 AM", "2:32", "Monday")
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30")
add_time("11:43 PM", "24:20", "tueSday")
add_time("6:30 PM", "205:12")



























