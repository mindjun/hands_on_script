# -*- coding:utf-8 -*-


import random


# -----------------------------
#        \   ^__^
#         \  (oo)\_______
#            (__)\       )\/\
#                ||----w |
#                ||     ||


def insert_sort():
    list1 = [random.randint(-500, 1000) for i in range(1000)]
    # for index,item in enumerate(list1):
    #     j = index
    #     while j > 0 and list1[j-1] > list1[j]:
    #         list1[j-1],list1[j] = list1[j],list1[j-1]
    #         j -= 1
    # print list1

    for index, item in enumerate(list1):
        while index > 0 and list1[index - 1] > item:
            list1[index] = list1[index - 1]
            index -= 1
        list1[index] = item
    print(list1)


# insert_sort()
# ========================================================


def bubble_sort():
    list1 = [random.randint(10, 100) for _ in range(10)]
    for i in range(0, len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
    print(list1)


# bubble_sort()


# ========================================================


def quick_sort(list1, l, u):
    if l >= u:
        return
    i, j = l, u
    target = list1[l]
    while i != j:
        while i < j and list1[j] >= target:
            j -= 1
        while i < j and list1[i] <= target:
            i += 1
        list1[i], list1[j] = list1[j], list1[i]
    list1[j] = target
    quick_sort(list1, 0, i - 1)
    quick_sort(list1, i + 1, u)


list1 = [random.randint(-100, 100) for i in range(10)]

quick_sort(list1, 0, len(list1) - 1)
print(f'here quick sort{list1}')


# ========================================================


def quickSortV2(list1, l, u):
    if l >= u:
        return
    m = l
    for i in range(l + 1, u + 1):
        if list1[i] < list1[l]:
            m += 1
            if i != m:
                list1[m], list1[i] = list1[i], list1[m]
    list1[m], list1[l] = list1[l], list1[m]
    quickSortV2(list1, l, m - 1)
    quickSortV2(list1, m + 1, u)


# list1 = []
# import time
# list1 = [random.randint(-100,100) for i in range(50)]
# start = int(time.time())
# quickSortV2(list1,0,len(list1)-1)
# print int(time.time()) - start
# print list1

# ========================================================

def selectSort():
    list1 = [random.randint(10, 100) for i in range(10)]
    for i in range(0, len(list1)):
        minNow = i
        for j in range(i + 1, len(list1)):
            # if list1[j] < list1[minNow]:
            if list1[j] > list1[minNow]:
                minNow = j
        list1[minNow], list1[i] = list1[i], list1[minNow]
    print(list1)


selectSort()


# ========================================================
# 最大堆实现
def adjustHeap(list1, i, size):
    lchild = i * 2 + 1
    rchild = i * 2 + 2
    maxNow = i
    if i < size / 2:
        if lchild < size and list1[lchild] > list1[maxNow]:
            maxNow = lchild
        if rchild < size and list1[rchild] > list1[maxNow]:
            maxNow = rchild
        if maxNow != i:
            list1[maxNow], list1[i] = list1[i], list1[maxNow]
            adjustHeap(list1, maxNow, size)


def buildHeap(list1, size):
    for i in range(0, size / 2)[::-1]:
        adjustHeap(list1, i, size)


def heapSort():
    list1 = [random.randint(10, 100) for i in range(10)]
    size = len(list1)
    buildHeap(list1, size)
    print('*' * 20)
    print(list1)
    for i in range(0, size)[::-1]:
        list1[0], list1[i] = list1[i], list1[0]
        adjustHeap(list1, 0, i)
    print(list1)


heapSort()


# ========================================================
# 最小堆

def adjustminHeap(list1, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    minNow = i
    if i < size / 2:
        if lchild < size and list1[lchild] < list1[minNow]:
            minNow = lchild
        if rchild < size and list1[rchild] < list1[minNow]:
            minNow = rchild
        if minNow != i:
            list1[minNow], list1[i] = list1[i], list1[minNow]
            adjustminHeap(list1, minNow, size)


# print (list1)
# size = len(list1)
# print (size)
# for i in range(0,5)[::-1]:
# adjustminHeap(list1,i,size)
# print (list1)


def buildminHeap(list1, size):
    for i in range(0, size / 2)[::-1]:
        adjustminHeap(list1, i, size)


def minHeapSort():
    list1 = [random.randint(0, 100) for i in range(10)]
    list2 = []
    size = len(list1)
    buildminHeap(list1, size)
    for i in range(0, size)[::-1]:
        list1[0], list1[i] = list1[i], list1[0]
        list2.append(list1[i])
        adjustminHeap(list1, 0, i)
    print(list1)
    print(list2)


# minHeapSort()
# ========================================================

def merge(left, right):
    result = []
    left.reverse()
    right.reverse()
    while len(left) > 0 and len(right) > 0:
        if left[-1] <= right[-1]:
            result.append(left[-1])
            del left[-1]
        else:
            result.append(right[-1])
            del right[-1]
    result.extend(left)
    result.extend(right)
    return result


list1 = [random.randint(10, 100) for i in range(10)]


def mergeSort(list1):
    if len(list1) <= 1:
        return list1
    mid = len(list1) / 2
    left = mergeSort(list1[:mid])
    right = mergeSort(list1[mid:])
    return merge(left, right)


# print mergeSort(list1)

# ========================================================

def bucketSort(list1):
    maxitem = max(list1)
    result = [0 for item in range(0, maxitem + 1)]
    print(len(result))
    list2 = []
    for item in list1:
        result[item] = result[item] + 1
    print(result)
    for index, item in enumerate(result):
        for i in range(1, item + 1):
            list2.append(index)
    print(list1)


list1 = [random.randint(10, 20) for i in range(10)]


# bucketSort(list1)

# ========================================================
# import collections
# print dir(collections)
# print help(collections.deque)
# ========================================================
# print random.random()
# import random
# # print help(random.seed)
# print random.seed(a=10)
# print random.randint(10,20)
# print hash(time.time())
# print int(50 + (120-50)*random.random())
# ========================================================

def select(m, n):
    import random
    for i in range(0, n + 1):
        if (random.randint(10000, 10000000) % n) < m:
            print(i)
            m -= 1
        if m == 0:
            break
        n -= 1


# select(5,20)

# ========================================================

def setSelect(m, n):
    import random
    set1 = set()
    while len(set1) < m:
        set1.add(random.randint(0, n))
    print(sorted(list(set1)))


# print dir(set)
# setSelect(5,20)

# ========================================================
def swapSelect(m, n):
    import random
    list1 = []
    for i in range(n + 1):
        list1.append(i)
    for j in range(0, m):
        s = random.randint(m, n)
        list1[s], list1[j] = list1[j], list1[s]
    # for i in range(0,m):
    #     list2.append(list1[i])
    print(list1[:m:])


# swapSelect(100,10000)
# ========================================================
# import timeit
# print timeit.timeit("x = sum(range(1000))")

# ========================================================
# import os
# print __file__
# print os.path.split(os.path.realpath(__file__))

# ========================================================
# from itertools import repeat
# rows = repeat(range(10), 10)
# print(type(rows))
# print([item for item in rows])

# ========================================================
# import hashlib
# sign_hashlib = hashlib.md5('test')
# sign_value = sign_hashlib.hexdigest()
# print sign_value.upper()
# ========================================================

# dict1 = dict()
# dict1.update({'a':1,'b':2,'c':3})
# print dict1['w']
# ========================================================
# import re
# ch = re.compile(u'[\u4e00-\u9fa5]+')
# print ch.search(u'你好')
# text = u'你好'
# print re.match(u'[\u4e00-\u9fa5]+', text)

# ========================================================
# import numpy
# import cv2

# hui = cv2.imread('hui.png', 1)
# # arr = numpy.asarray(hui, dtype="float32")
# data = numpy.empty((4, hui.shape[0], hui.shape[1], 3), dtype='int')
# print data[0]
# data[0] = hui
# print data[0]

# scaleBig = numpy.max([hui.shape[0], hui.shape[1]])
# print scaleBig


# ========================================================
# a = np.arange(24).reshape((2, 3, 4))
# print a
# b = a[1][1][1]
# print b

# c = a[:, 2, :]
# print c

# g = np.split(np.arange(9), 3)
# print g

# h = np.split(np.arange(9), [2, -3])
# print h
# b = np.sin(np.pi/2)
# print b
# a = np.array([3, 4])
# print np.linalg.norm(a)

# x_data = np.float32(np.random.rand(2, 100))
# y_data = np.dot([0.100, 0.200], x_data) + 0.300

# print x_data
# print '='*20
# print y_data

# ========================================================
# import logging
# print dir(logging.log)

# ========================================================
# dict1 = dict()
# dict1.update({'a':1,'b':2})

# print('environment information:{0}'.format(dict1))

# ========================================================
# from linked import *
# print request_param_list
# ========================================================
from datetime import datetime

current_time = datetime.now()
nowday = datetime.today()
# print nowday
# 当前日期，用于拼接保存文件的路径
today = current_time.strftime('%Y%m%d')


# print current_time.strftime('%Y-%m-%d %H:%M:%S')
# print today

# ========================================================

# import uuid
# print uuid.uuid1()

# ========================================================
# list1 = [i for i in range(10)]
# print list1
# def filter_list(list1):
#     list1.pop()

# filter_list(list1)
# # print list1

# ========================================================
# from pygorithm import searching, sorting
# from pygorithm.sorting import heap_sort
# # print dir(sorting)
# mylist = [random.randint(10,100) for i in range(10)]
# sortList = heap_sort.sort(mylist)
# print sortList
# code = heap_sort.get_code()
# print code

# ========================================================
# import os
# cur_path = os.path.abspath('')
# print cur_path
# path = os.path.join(cur_path, 'log')
# print path
# print os.path.abspath(os.path.dirname(__file__))
# import sys
# print sys.platform

# ========================================================


class SingleTon(object):
    """docstring for SingleTon"""

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingleTon, cls).__new__(cls)
        return cls.instance


obj1 = SingleTon()
obj2 = SingleTon()


# obj1.attr1 = 'test'
# print obj1.attr1, obj2.attr1
# print obj1 is obj2

# ========================================================


# print math.pi

# ========================================================
# print [(i,j) for i in range(4) for j in range(4)]

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


recurse(3, 0)

# ========================================================
# def draw(t, length, n):
#     if n == 0:
#         return
#     angle = 50
#     t.fd(length*n)
#     t.lt(angle)
#     draw(t, length, n-1)
#     t.rt(2*angle)
#     draw(t, length, n-1)
#     t.lt(angle)
#     t.bk(length*n)

# import turtle
# bob = turtle.Turtle()
# draw(bob, 100, 2)
# turtle.mainloop()
# ========================================================
# str1 = 'abctxyz'
# str2 = 'xyztc'
# print [item for item in str1 if item in str2]

# ========================================================

# 计数排序，有点类似于桶排序，但是不需要那么桶，时间复杂度取决于序列中数的范围
from collections import defaultdict


def counting_sort(A, key=lambda x: x):
    B, C = [], defaultdict(list)
    count = 0
    for item in A:
        C[key(item)].append(item)
    for k in range(min(C), max(C) + 1):
        count += 1
        B.extend(C[k])
    print(count)
    return B


# list1 = [random.randrange(10, 1000) for i in range(10)]
# list1.extend(list1[:len(list1)//2:])
# print(list1)
# print(max(list1) - min(list1))
# print(counting_sort(list1))

# ========================================================
# 朴素版拓补排序
G = [
    {'b', 'f'},
    {'c', 'd'},
    {'d'},
    {'e', 'f'},
    {'f'},
    {}
]


def naiva_topsort(G, S=None):
    if S is None:
        S = set(G)
    if len(S) == 1:
        return list(S)
    v = S.pop()
    seq = naiva_topsort(G, S)
    min_i = 0
    for i, u in enumerate(seq):
        if v in G[u]:
            min_i = i + 1
    seq.insert(min_i, v)
    return seq


print(naiva_topsort(G))
