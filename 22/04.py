import datetime

time_to_bd = datetime.datetime.now() + datetime.timedelta(days=int(input()))
print(time_to_bd.day, time_to_bd.month)
