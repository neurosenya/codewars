import re

def format_duration(seconds):
    minute = 60
    hour = minute * 60 # seconds
    day = hour * 24
    year = day * 365
    res = []
    years = seconds // year
    left_seconds = seconds - year*years
    res.append(("years", years))

    days = left_seconds // day
    left_seconds = left_seconds - day*days
    res.append(("days", days))

    hours = left_seconds // hour
    left_seconds = left_seconds - hour*hours
    res.append(("hours", hours))

    minutes = left_seconds // minute
    left_seconds = left_seconds - minute*minutes
    res.append(("minutes", minutes))
    res.append(("seconds", left_seconds))
    f = [i if i[1] > 1 else (i[0][:-1], i[1]) for i in res]
    f = [i for i in f if i[1] > 0]
    s = ", ".join([str(i[1]) +" "+ str(i[0]) for i in f])
    if len(f) > 1:
        regex = re.compile(r", \d+ [a-z]*$")
        s = regex.sub(r" and " + str(f[-1][1]) + " " + f[-1][0], s)
    return s

print(format_duration(1))
