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


def coin_change(coins, amount):
    dp = [amount + 1 for _ in range(amount + 1)]
    dp[0] = 0
    result = defaultdict(list)
    for n in range(0, amount + 1):
        for coin in coins:
            if n - coin < 0:
                continue
            # dp[n] = min(dp[n], 1 + dp[n - coin])
            if dp[n] < 1 + dp[n - coin]:
                continue
            else:
                dp[n] = 1 + dp[n - coin]
                result[n].append(coin)
    return dp, result


print('coin_change ', coin_change([1, 2, 5], 11))


# def sliding_windows(s, t):
#     need, windows = defaultdict(int), defaultdict(int)
#     for c in t:
#         need[c] += 1
#     left, right = 0, 0
#     valid = 0
#     while right < len(s):
#         char = s[right]
#         right += 1
#         # 进行窗口的更新
#
#         # 判断左侧窗口是否需要收缩
#         while left:
#             d = s[left]
#             left += 1
#             # 进行窗口内数据的更新


def sliding_windows(s, t):
    need, windows = defaultdict(int), defaultdict(int)
    for c in t:
        need[c] += 1
    left, right = 0, 0
    valid = 0
    start, length = 0, len(s) + 1
    while right < len(s):
        c = s[right]
        right += 1
        # 进行窗口的更新
        if c in need:
            windows[c] += 1
            if windows[c] == need[c]:
                valid += 1

        # 判断左侧窗口是否需要收缩
        while valid == len(need):
            if right - left < length:
                start = left
                length = right - start
            d = s[left]
            left += 1
            # 进行窗口内数据的更新
            if d in need:
                if need[d] == windows[d]:
                    valid -= 1
                windows[d] -= 1
    if length == len(s) + 1:
        return ""
    else:
        return s[start: start + length]


class MaxSlideQueue(object):
    def __init__(self):
        self.queue = list()

    def push(self, item):
        while self.queue and self.queue[-1] < item:
            self.queue.pop()
        self.queue.append(item)

    def max(self):
        return self.queue[0]

    def pop(self, item):
        # 只有当 item 是最大的值时才删除
        if self.queue[0] == item:
            self.queue = self.queue[1:]


# max slide windows
def max_slide_windows(list1, size):
    result = list()
    slide_windows = MaxSlideQueue()
    for index, item in enumerate(list1, 1):
        if index < size:
            slide_windows.push(item)
        else:
            slide_windows.push(item)
            result.append(slide_windows.max())
            # pop 的 item 应该是 index - k
            slide_windows.pop(list1[index - size])
    return result


print(f'max_slide_windows ', max_slide_windows(list1=[1, 3, -1, -3, 5, 3, 6, 7], size=3))


# 回溯算法
# 明确路径（已经遍历，选择过的元素） 选择列表（剩下可选择的元素） 结束条件
# for 选择 in 选择列表:
#     # 做选择
#     将该选择从选择列表移除
#     路径.add(选择)
#     backtrack(路径, 选择列表)
#     # 撤销选择
#     路径.remove(选择)
#     将该选择再加入选择列表

# 全排列
# // 路径：记录在 track 中
# // 选择列表：nums 中不存在于 track 的那些元素
# // 结束条件：nums 中的元素全都在 track 中出现
def permute(list1):
    _track, res = list(), list()

    def back_track(choice_list, track):
        # len(choice_list) - 1 表示从 choice_list 中选出 (len(choice_list) - 1) 个元素进行排列
        if len(track) == len(choice_list) - 1:
            res.append(list(track))
            return

        for choice in choice_list:
            if choice in track:
                continue
            track.append(choice)
            back_track(choice_list, track)
            track.pop()

    back_track(list1, _track)
    return res


print(f'permute for [1, 2, 3], A(3, 2) is {permute([1, 2, 3])}')


# 组合
# 输入两个数字 n, k，算法输出 [1..n] 中 k 个数字的所有组合。
def combine(n, k):
    res, _track = list(), list()
    if n <= 0 or k <= 0:
        return res

    # start 用来标记已经遍历过的数
    def back_track(start, track):
        if len(track) == k:
            res.append(track.copy())
            return
        for i in range(start, n + 1):
            track.append(i)
            back_track(i + 1, track)
            track.pop()

    # 从 1 开始
    back_track(1, _track)

    return res


print(f'combine for [1, 2, 3], C(3, 2) is {combine(3, 2)}')


# 计算子集
# A = subset([1,2])
# subset([1,2,3]) = A + [A[i].add(3) for i = 1..len(A)]
def subset(_nums):
    _res = list()

    def recursive(nums, _res):
        # base case，返回一个空数组
        if not nums:
            _res.append([])
            return
        n = nums.pop()
        recursive(nums, _res)
        temp = list(deepcopy(_res))
        for i in temp:
            i.append(n)
        _res += temp

    recursive(_nums, _res)
    return _res


print(subset([1, 2, 3]))


def subset_backtrack(nums):
    res = list()

    def back_track(_nums, start, track):
        res.append(list(track))
        for i in range(start, len(_nums)):
            track.append(nums[i])
            back_track(_nums, i + 1, track)
            track.pop()

    back_track(nums, 0, [])
    return res


print(subset_backtrack([1, 2, 3]))


def generate_parenthesis(n):
    _res, _track = list(), list()

    def back_track(left, right, track, res):
        if right < left:
            return
        if left < 0 or right < 0:
            return
        if left == 0 and right == 0:
            res.append(track.copy())

        track.append('(')
        back_track(left - 1, right, track, res)
        track.pop()

        track.append(')')
        back_track(left, right - 1, track, res)
        track.pop()

    back_track(n, n, _track, _res)
    return _res

    # 返回所有的组合情况
    # def back_track(n, i, stack):
    #     if i == 2 * n:
    #         _res.append(stack.copy())
    #         return
    #
    #     for choice in ['(', ')']:
    #         stack.append(choice)
    #         generate_parenthesis(n, i + 1, stack)
    #         stack.pop()


print(generate_parenthesis(3))


def generate_parenthesis_v1(n: int) -> List[str]:
    result = list()

    def helper(left, right, s):
        if len(s) == 2 * n:
            result.append(s)
            return

        if left < n:
            helper(left + 1, right, s + '(')

        if right < left:
            helper(left, right + 1, s + ')')

    helper(0, 0, '')
    return result


print(generate_parenthesis_v1(3))


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


def length_of_lis(nums):
    """
    最长上升子序列
    :param nums:
    :return:
    """
    # dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度
    dp = [1 for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in list(range(0, i)):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    res = 0
    for i in range(len(nums)):
        res = max(res, dp[i])
    return res


# dp == [1, 2, 2, 3, 2, 3]
print(length_of_lis([1, 4, 3, 4, 2, 3]))


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


# 计算 1 至 n 中数字 x 出现的次数 x in range(0, 10)
# def count(n, x):
#     res, i = 0, 1
#
#     def helper(_n, _i):
#         len_str = len(str(_n))
#         if _i < 10:
#             return 1 if x < _i else 0
#         while True:
#             part_1 = pow(10, len_str)
# https://www.cnblogs.com/duanxz/p/9662862.html
def count(n, x):
    cnt, k, i = 0, n, 1
    while True:
        cnt += int(k / 10) * i
        cur = k % 10
        if cur > x:
            cnt += i
        elif cur == x:
            # 2500 -- 2593 ==> 94
            cnt += n % i + 1
        i *= 10
        k = int(n / i)
        if k < 10:
            break
    return cnt


print(count(2593, 5))


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


print(get_res(a="11", b="1"))


def add_binary(a, b) -> str:
    x, y = int(a, 2), int(b, 2)
    while y:
        answer = x ^ y
        carry = (x & y) << 1
        x, y = answer, carry
    return bin(x)[2:]


print(add_binary(a="1010", b="1011"))
