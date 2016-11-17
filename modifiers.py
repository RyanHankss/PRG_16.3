class Time(object):

    """
    The time of day.
    attributes: hour, minute, second
    """


def time_int(time):
    seconds = (time.hour * 60 * 60) + (time.minute * 60) + time.second
    return seconds


def increment(time, seconds):
    seconds += time_int(time)
    return seconds


def print_this(t):
    print('{}.{}.{}'.format(t.hour, t.minute, t.second))


def int_time(seconds):
    tt = Time()
    tt.hour = seconds/ (60 * 60)
    secs = seconds % (60 * 60)
    tt.minute = secs / 60
    tt.second = secs % 60
    return tt

start = Time()
start.hour = 11
start.minute = 58
start.second = 11


print_this(start)

end = increment(start, 1572)
incr_time = int_time(end)
print_this(incr_time)
