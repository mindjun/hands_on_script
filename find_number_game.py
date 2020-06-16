import math
"""
游戏方法，用于猜数字，思路为使用二分法逐步缩小范围
"""


def find_n(target, max_num):
    bili, count = 1/2, 1
    p = max_num * bili
    while p != target and (p-1) != target:
        print(p)
        count += 1
        if p < target:
            print('small')
            bili += math.pow(2, -count)
            print(bili)
        elif p > target:
            print('big')
            bili -= math.pow(2, -count)
            print(bili)
        # 防止出现p为小数，不方便比较的情况
        p = math.ceil(max_num * bili)
    print(count)
    p = p if p == target else p-1
    print('find target is {}'.format(p))
