class Time(object):

    """
    Represents the time of day.
    attributes: hour, minute, second
    """


t1 = Time()
t1.hour = 11
t1.minute = 18
t1.second = 20

t2 = Time()
t2.hour = 13
t2.minute = 30
t2.second = 20


def increment(time, seconds):
    time.hour = seconds/(60 * 60)
    time.minute = seconds/60
    time.second = seconds % (60 * 60)
    if time.hour > 23:
        time.hour = 0
    if time.minute > 60:
        time.hour += 1
    if time.second > 60:
        time.minute += 1


print increment(t1, 0)
