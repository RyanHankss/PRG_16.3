class Time(object):

    """
    Represents the time of day.
    attributes: hour, minute, second
    """


def increment(time, second):
    time.second += second
    time.minute += time.second//60
    time.hour += time.minute//60
    time.second %= 60
    time.minute %= 60
    time.hour %= 24


print increment('11', '49')
