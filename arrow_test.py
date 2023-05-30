import time


def time_diff(begin_time, end_time):
    if begin_time < end_time:
        start_time = begin_time
        endtime = end_time
    else:
        start_time = end_time
        endtime = begin_time

    # 计算天数
    timediff = endtime - start_time
    days = (timediff // 86400)
    # 计算小时数
    remain = timediff % 86400
    hours = (remain // 3600)
    # 计算分钟数
    remain = remain % 3600
    _min = (remain // 60)
    # 计算秒数
    secs = remain % 60
    _res = {"day": days, "hour": hours, "min": _min, "sec": secs}
    return _res


start = int(time.time())
end = int(time.time()) - 8908
res = time_diff(start, end)
# {'days': 0, 'hours': 2, 'minutes': 28, 'seconds': 28}
print(res)
