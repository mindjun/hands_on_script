import random
import math
import copy


def build_heap(l, i, s):
    lc = i*2 + 1
    rc = i*2 + 2
    now = i
    if i < s/2:
        if lc < s and l[lc] < l[now]:
            now = lc
        if rc < s and l[rc] < l[now]:
            now = rc
        if now != i:
            l[i], l[now] = l[now], l[i]
            build_heap(l, now, s)


list1 = [random.randint(0,20) for _ in range(10)]
length = len(list1)
# print(list1)
# 构建最小堆
for ii in range(0, int(length/2))[::-1]:
    build_heap(list1, ii, length)

# print(list1)


# 找到前k小的元素
k = 5
all_list = [random.randint(0,50) for _ in range(30)]
copy_list = copy.deepcopy(all_list)
heap_list = all_list[:k]

print(all_list)


# def adjust_heap():
#     for i in range(0, math.ceil(k/2))[::-1]:
#         build_heap(heap_list, i, k)
#
#
# for item in all_list[k:]:
#     now_max = max(heap_list)
#     if item < now_max:
#         heap_list.remove(now_max)
#         heap_list.append(item)
#         adjust_heap()
#
# print(heap_list)
# all_list.sort()
# print(all_list[:5])

length = len(all_list)
half = math.ceil(length/2)
for ii in range(0, half)[::-1]:
    build_heap(all_list, ii, length)


for i in list(range(0,14)):
    if all_list[i] > min((all_list[i*2+1], all_list[i*2+2])):
        print('error')

print(all_list)
print(all_list[:5])
copy_list.sort()
print(copy_list[:5])

