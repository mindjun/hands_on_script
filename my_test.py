from functools import lru_cache


@lru_cache(maxsize=10)
def my_func(a):
    print('here')
    return sum(a)


res = my_func(range(1000000000))
print(res)
print(my_func(range(1000000000)))


str1 = '[0, 1000],[1001, 4000),[4000,5000]'
num_list = [0, 1000, 1001, 4000, 4000, 5000]
parr_list = ['[', ']', '[', ')', '[', ']']

# 保证升序
sub_list = [b - a > 0 for a,b in zip(num_list[::2], num_list[1::2])]
print(sub_list)

# 有以下几种情况
# ] [ 两个值差1
# ] ( 两个值相等
# ) [ 两个值相等
# ) ( 错误

# 保证开闭区间
# temp_num = num_list[1:]
# temp_parr = parr_list[1:]
#
# num_tuple = list(zip(temp_num[1::2], temp_num[::2]))
# # print(num_tuple)
# len_ = len(parr_list[1::2])
# for a, b, index in zip(temp_parr[::2], temp_parr[1::2], range(int(len_))):
#     if a == ']' and b == '[' and num_tuple[index][0] - num_tuple[index][1] != 1:
#         print('error')
#     elif a == ']' and b == '(' and num_tuple[index][0] != num_tuple[index][1]:
#         print('error')
#     elif a == ')' and b == '[' and num_tuple[index][0] != num_tuple[index][1]:
#         print('error')
#     elif a == ')' and b == '(':
#         print('error')
#     else:
#         print('right')


# import pandas as pd

import random

pa = [item for item in 'abcdef']
cols = {'sys_init': [random.randint(100, 120) for _ in range(6)],
        'dia_init': [random.randint(100, 120) for _ in range(6)],
        'sys_fin': [random.randint(100, 120) for _ in range(6)],
        'dia_fin': [random.randint(100, 120) for _ in range(6)]}

print([random.randint(100, 120) for _ in range(6)])
