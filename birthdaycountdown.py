import time
print('Hey there! Welcome to the birthday counter.')
try:
    year = int(input("What year were you born in?\n"))
    month = int(input("What month were you born in?(1 for Jan, 2 for Feb, so on...)?\n"))
    day = int(input("What day of that month were you born in?\n"))

    import datetime as dt
    date_of_birth = dt.datetime(year, month, day)

    weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_num = date_of_birth.weekday()
    print("You may have forgotten the day on which you were born.")
    print("But I know, you were born on a ... ", end = '')
    print(weekday_names[weekday_num]) 

    current_time = dt.datetime.now()
    thisyear = current_time.year
    thisyear_bday = dt.datetime(thisyear, month, day)
    
    diff = (current_time - date_of_birth).days
    age = diff//365
    print('You are ', age, 'years old.')
    
    if thisyear_bday > current_time:
            next_bday = thisyear_bday
    else:
        next_bday = dt.datetime(thisyear+1, month, day)
    test_year = date_of_birth.year + 1
    bday_list = [0, 0, 0, 0, 0, 0, 0]
    
    while test_year < next_bday.year:
         test_date = dt.datetime(test_year, month, day)
         weekday_num = test_date.weekday()
         bday_list[weekday_num] = bday_list[weekday_num] + 1
         test_year = test_year + 1
    print()
    for kk in range(7):
         print('Your birthday was on a ', weekday_names[kk], bday_list[kk], 'times.')
    print()
        
    print("Your next birthday will be on...", end = '')
    print(next_bday)
    print("That will be on a ... ", end = '')
    weekday_num = next_bday.weekday()
    print(weekday_names[weekday_num])

    dd = next_bday - current_time
    days_left = dd.days
    total_seconds_left = dd.seconds

    seconds_left = total_seconds_left%60
    total_mins_left = total_seconds_left//60
    hrs_left = total_mins_left//60
    mins_left = total_mins_left%60

    total_mins_left, seconds_left = divmod(total_seconds_left, 60)
    hrs_left, mins_left = divmod(total_mins_left, 60)

    while next_bday > current_time:
        current_time = dt.datetime.now()
        dd = next_bday - current_time
        days_left = dd.days
        total_seconds_left = dd.seconds
            
        seconds_left = total_seconds_left%60
        total_mins_left = total_seconds_left//60
        hrs_left = total_mins_left//60
        mins_left = total_mins_left%60

        print('Your next birthday is ', days_left, 'days, ', hrs_left, 'hours, ', mins_left, 'minutes, and ', seconds_left, 'seconds away.', end = '\r')
            
        time.sleep(1)

except:
     print("That is an invalid value. Please enter a valid value and start again.")
