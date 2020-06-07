def timediff(begin_time,end_time):

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
    min = (remain // 60)
    # 计算秒数
    secs = remain % 60
    res = {"day": days, "hour": hours, "min": min, "sec": secs}
    return res


import time

start = int(time.time())
end = int(time.time()) - 8908
res = timediff(start, end)
# {'days': 0, 'hours': 2, 'minutes': 28, 'seconds': 28}
print(res)
