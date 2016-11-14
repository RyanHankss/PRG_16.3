class Time(object):

    """
    Represents the time of day.
    attributes: hour, minute, second
    """

def increment(time, seconds):
    hour = seconds/(60 * 60)
    minute = seconds/60
    seconds =  seconds % (60 * 60)
    if time.hour > 23:
        time.hour = 0
    if time.minute > 60
        time.hour += 1
    if time.second > 60
        time.minute += 1
    
    

def increment(time, second):
    time.second += second
    time.minute += time.second//60
    time.hour += time.minute//60
    time.second %= 60
    time.minute %= 60
    time.hour %= 24


print increment()
