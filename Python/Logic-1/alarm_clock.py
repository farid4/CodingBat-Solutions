def alarm_clock(day, vacation):
    weekdays = "10:00" if vacation else "7:00"
    weekends = "off" if vacation else "10:00"
    
    if 1 <=  day and day <= 5:
        return weekdays
                
    return weekends
