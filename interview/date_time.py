import time
import datetime


# float --> struct tuple
time_tuple = time.localtime()
print(time_tuple[-3])
print(time.localtime(time.time()))

# struct time tuple --> str
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

print(datetime.datetime.now())

# 获取本周最后一天
today = datetime.date.today()
last_day1 = today + datetime.timedelta(6-today.weekday())
print(last_day1)

# 获取本月最后一天
import calendar
_, last_day_num = calendar.monthrange(today.year, today.month)
last_day2 = datetime.date(today.year, today.month, last_day_num)
print(last_day2)

# 获取上个月最后一天
first = datetime.date(day=1, month=today.month, year=today.year)
last_month = first - datetime.timedelta(days=1)
print(last_month)
