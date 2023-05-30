import heapq
import math
import random
from copy import deepcopy
from collections import Counter, defaultdict
from functools import wraps
from typing import List


class SingleTon(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingleTon, cls).__new__(cls, *args, **kwargs)
        return cls._instance


# -123 --> -321
def reverse_int(i):
    is_negative = False
    if i < 0:
        is_negative = True

    reverse = int(math.fabs(i))
    reverse_1 = reverse
    result_list = list()
    while reverse > 10:
        result_list.append(reverse % 10)
        reverse = reverse // 10
    result_list.append(reverse)

    if is_negative > 10:
        length = len(str(i))
    else:
        length = len(str(i)) - 1

    res = 0
    res1 = 0
    while length >= 0:
        temp = reverse_1 % 10
        res += temp * pow(10, length - 1)
        if length != 0:
            res1 = res1 * 10 + temp
        reverse_1 = reverse_1 // 10
        length -= 1
    print(res)
    print(res1)

    return result_list


print(reverse_int(-123))


# "123" ==> 123 不使用 int 方法
# ord str ==> ASCII
# chr ASCII ==> str
def atoi(s):
    num = 0
    for v in s:
        num = num * 10 + ord(v) - ord('0')
    return num


print(atoi("123"))


# 给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] = 2+7 =9,所以返回[0,1]
def two_sun(list1, target):
    dict1 = {item: i for i, item in enumerate(list1)}
    for index, item in enumerate(list1):
        if (target - item) in dict1:
            return index, dict1.get((target - item))
    return ()


def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return left, right
    return ()


print(two_sun([2, 7, 11, 15], 9))
print(two_sum([2, 7, 11, 15], 7))


# https://leetcode-cn.com/problems/3sum/
def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = list()

    for k in range(len(nums) - 2):
        if nums[k] > 0:
            break
        if k > 0 and nums[k] == nums[k - 1]:
            continue

        i, j = k + 1, len(nums) - 1
        while i < j:
            s = nums[k] + nums[i] + nums[j]
            if s < 0:
                i += 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
            elif s > 0:
                j -= 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
            else:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                # 避免有重复的值，在循环前进行判断
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
    return res


def find_second_large_num(list1):
    return heapq.nlargest(2, list1)


list_ = list(range(1, 100))
print(find_second_large_num(list_))

print(Counter('AAABBCCAC').most_common(2))


def multipliers():
    for i in range(4):
        yield lambda x: i * x


print([i(2) for i in multipliers()])


def multipliers():
    return [lambda x, i=i: i * x for i in range(4)]


print([i(2) for i in multipliers()])


def adjust_heap(list1, i, size):
    while i < size / 2:
        left, right = i * 2 + 1, i * 2 + 2
        min_item = i
        if left < size and list1[left] < list1[min_item]:
            min_item = left
        if right < size and list1[right] < list1[min_item]:
            min_item = right
        if min_item == i:
            return
        else:
            list1[i], list1[min_item] = list1[min_item], list1[i]
            i = min_item


def build_heap(list1):
    size = len(list1)
    for i in range(0, size // 2)[::-1]:
        adjust_heap(list1, i, size)


def top_n_min(n, list1):
    build_heap(list1)
    result = list()
    size = len(list1)
    while n != 0:
        size -= 1
        list1[0], list1[size] = list1[size], list1[0]
        result.append(list1[size])
        adjust_heap(list1, 0, size)
        n -= 1
    return result


# _list = list(range(10, 20))
# random.shuffle(_list)
# print(_list)
# print(build_heap(_list))
# print(_list)


_list = [random.randint(10, 100) for _ in range(20)]
print(f'heap sort info : {_list}')
print(f'heap sort top 3 min is : {top_n_min(3, _list)}')


def quick_sort(list1, l, r):
    if l > r:
        return
    i, j = l, r
    target = list1[l]
    while i != j:
        while i < j and list1[j] > target:
            j -= 1
        while i < j and list1[i] < target:
            i += 1
        list1[i], list1[j] = list1[j], list1[i]
    list1[i], list1[l] = list1[l], list1[i]
    quick_sort(list1, 0, i - 1)
    quick_sort(list1, i + 1, r)


def singleton(cls):
    instance = dict()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


def point_24(target=24):
    all_options = ['7 7 3 3', '8 8 3 3', '5 5 5 1', '1 5 7 10', '2 5 5 10']
    all_options = [i.split() for i in all_options]
    all_operations = list('+-*/')
    result = list()
    for item in all_options:
        for op1 in all_operations:
            for op2 in all_operations:
                for op3 in all_operations:
                    express = f"{item[0]}{op1}{item[1]}{op2}{item[2]}{op3}{item[3]}"
                    print(express)
                    print(eval(express))
                    if eval(express) == target:
                        result.append(express)
    return result


def next_greater_element(list1):
    size, stack = len(list1), list()
    result = [-1 for _ in range(size)]
    for i in range(size * 2 - 1)[::-1]:
        while stack and stack[-1] <= list1[i % size]:
            stack.pop()
        result[i % size] = -1 if not stack else stack[-1]
        stack.append(list1[i % size])
    print(stack)
    return result


print(f'next_greater_element {next_greater_element([2, 1, 2, 4, 3])}')


def is_sub_sequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


# 烧饼排序
# https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/shao-bing-pai-xu
def shao_bing_sort(nums):
    n = len(nums)
    res = list()

    while n > 1:
        temp_max, max_index = 0, 0
        for index, item in enumerate(nums[:n]):
            if item > temp_max:
                temp_max = item
                max_index = index
        res.append(max_index + 1)
        # 翻转 0 ... max_index
        nums = nums[:max_index + 1][::-1] + nums[max_index + 1:]
        # 翻转 0 ... n
        res.append(n)
        nums = nums[:n][::-1] + nums[n:]
        n -= 1
    print(nums)
    return res


def shao_bing_sort1(cakes):
    res = list()

    def helper(n, nums):
        # base case
        if n == 1:
            return
        temp_max, max_index = 0, 0
        for index, item in enumerate(nums[:n]):
            if item > temp_max:
                temp_max = item
                max_index = index

        res.append(max_index + 1)
        # 翻转 0 ... max_index
        reverse(nums, 0, max_index)
        # 翻转 0 ... n
        res.append(n)
        reverse(nums, 0, n - 1)

        # 递归调用
        helper(n - 1, nums)

    def reverse(nums, i, j):
        """
        翻转 i 到 j 位置的数据
        """
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    helper(len(cakes), cakes)
    print(cakes)
    return res


print(shao_bing_sort([3, 2, 4, 1]))
print(shao_bing_sort1([3, 2, 4, 1]))


# 前缀和
def sub_array_sum_0(nums, k):
    pre_sum = [0 for _ in range(len(nums) + 1)]
    ans = 0
    # pre_sum[j + 1] - pre_sum[i] 就是数组 i...j 的和
    for i in range(len(nums)):
        for j in range(i):
            if pre_sum[j] - pre_sum[i] == k:
                ans += 1
    return ans


def sub_array_sum(nums, k):
    pre_sum_dict = dict()
    pre_sum_dict[0] = 1

    ans, sum_i = 0, 0
    for index, item in enumerate(nums):
        sum_i += item
        sum_j = sum_i - k
        if sum_j in pre_sum_dict:
            ans += pre_sum_dict.get(sum_j)
        pre_sum_dict[sum_i] = pre_sum_dict.get(sum_i, 0) + 1
    return ans


class Solution:
    def jump(self, nums) -> int:
        # jumps = 0
        # size, i = len(nums), 0
        # while i < size - 1:
        #     jumps += 1
        #     if i + nums[i] >= size - 1:
        #         return jumps
        #     steps_list = [(item, index + i) for item, index in enumerate([nums[j] for j in range(i + nums[i])])]
        #     steps_list.sort(key=lambda x: x[0])
        #     i += steps_list[-1][-1]
        # return jumps

        # def dp(p):
        #     if p >= size - 1:
        #         return 0
        #     if memo[p] != size:
        #         return memo[p]
        #     steps = nums[p]
        #     for i in range(1, steps + 1):
        #         sub = dp(p + i)
        #         memo[p] = min(memo[p], sub + 1)
        #     return memo[p]
        #
        # size = len(nums)
        # memo = [size for _ in range(size)]
        # return dp(0)

        jumps, end, farthest = 0, 0, 0
        size = len(nums)
        for i in range(size - 1):
            farthest = max(farthest, nums[i] + i)
            if i == end:
                jumps += 1
                end = farthest
        return jumps


print(Solution().jump([2, 3, 1, 1, 4]))


# 输入: a = "1010", b = "1011"
# 输出: "10101"

def get_res(a, b):
    len_a, len_b = len(a), len(b)
    if len_a > len_b:
        b = b.zfill(len_a)
    else:
        a = a.zfill(len_b)

    flag, res = '0', ''
    for i, j in zip(a[::-1], b[::-1]):
        if i == '1' and j == '1':
            res = flag + res
            flag = '1'
        elif i == '0' and j == '0':
            res = flag + res
            flag = '0'
        #  (i == '0' and j == '1') or (i == '1' and j == '0')
        else:
            if flag == '1':
                res = '0' + res
            else:
                res = '1' + res
    if flag == '1':
        res = '1' + res
    return res


print(get_res(a="1010", b="1011"))


def add_binary(a, b) -> str:
    x, y = int(a, 2), int(b, 2)
    while y:
        answer = x ^ y
        carry = (x & y) << 1
        x, y = answer, carry
    return bin(x)[2:]


print(add_binary(a="1010", b="1011"))


def str_str(haystack: str, needle: str):
    if not needle:
        return 0
    i, j = 0, 0
    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle) + 1):
            if j < len(needle) and haystack[i+j] != needle[j]:
                break
        if len(needle) == j:
            return i
    return -1


print(str_str('hello', 'll'))


def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for n in range(1, amount + 1):
        for coin in coins:
            if n - coin < 0:
                continue
            dp[n] = min(dp[n], 1 + dp[n-coin])
    return dp


print(coin_change([1, 2, 5], 11))


def coin_change1(coins, amount):
    memo = dict()

    def dp(n):
        res = float("INF")
        if n == 0:
            return 0
        if n < 0:
            return -1
        if n in memo:
            return memo[n]

        for coin in coins:
            sub_problem = dp(n-coin)
            if sub_problem == -1:
                continue
            res = min(res, 1 + sub_problem)
        memo[n] = res if res != float("INF") else -1
        return memo[n]

    return dp(amount)


print(coin_change1([1, 2, 5], 11))
