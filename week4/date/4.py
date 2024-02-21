import datetime

time1 = datetime.datetime.now()
time2 = time1 - datetime.timedelta(days=2)
difference = time1 - time2

print(difference.total_seconds(), "seconds")