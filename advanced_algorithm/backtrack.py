"""
回溯法
解决一个回溯问题，实际上就是一个决策树的遍历过程

# https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/hui-su-suan-fa-xiang-jie-xiu-ding-ban
# https://github.com/dashidhy/algorithm-pattern-python/blob/master/advanced_algorithm/backtrack.md

result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
"""
from typing import List
from copy import deepcopy


# 全排列
# // 路径：记录在 track 中
# // 选择列表：nums 中不存在于 track 的那些元素
# // 结束条件：nums 中的元素全都在 track 中出现
# 没有重复的情况
def permute(board):
    _track, res = list(), list()
    # target_length 表示从 board 中选出 target_length 个元素进行排列
    target_length = len(board)

    def back_track(choice_list, track):
        if len(track) == target_length:
            res.append(list(track))
            return

        for choice in choice_list:
            if choice in track:
                continue
            track.append(choice)
            back_track(choice_list, track)
            track.pop()

    back_track(board, _track)
    return res


print(f'permute for [1, 2, 3], A(3, 2) is {permute([1, 2, 3])}')


# https://www.bilibili.com/video/BV1mY411D7f6/?vd_source=e0c4806c7843b66260ba282654cd8eba
def new_permute(nums):
    n = len(nums)
    res = []
    path = [0] * n

    def dfs(i, s):
        if i == n:
            res.append(list(path))

        for x in s:
            path[i] = x
            dfs(i+1, s-{x})

    dfs(0, set(nums))
    return res


print(f'new_permute for [1, 2, 3], A(3, 2) is {new_permute([1, 2, 3])}')


# https://leetcode-cn.com/problems/permutations-ii/submissions/
# https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-by-powcai-3/
# 存在重复字符的情况下，需要先排序，并且在回溯的时候需要判断该字符是否与前一个字符相等，避免重复处理
def permute_ii(nums):
    if not nums:
        return []

    _track, res = list(), list()
    nums.sort()
    size = len(nums)

    def helper(_nums, track, length):
        if length == size and track not in res:
            res.append(track)

        for i in range(len(_nums)):
            helper(_nums[:i] + _nums[i+1:], track + [_nums[i]], length + 1)

    def back_track(_nums, track):
        if not _nums:
            res.append(track.copy())
            return
        for idx, num in enumerate(_nums):
            if idx > 0 and _nums[idx] == _nums[idx - 1]:
                continue
            track.append(num)
            back_track(_nums[:idx] + _nums[idx + 1:], track)
            track.pop()

    # helper(nums, _track, 0)
    back_track(nums, [])
    return res


print(permute_ii([1, 1, 2]))


# 使用回溯的时候会遇到一些重复字符的错误
# 需要先进行排序
def permutation(s):
    if not s:
        return []

    result_list = list()

    def back_pack(s_, track):
        if not s_:
            result_list.append(''.join(track))
            return

        for idx, ch in enumerate(s_):
            # 有可能回出现重复的字符，如果当前的字符已经处理过，就跳过
            if idx > 0 and s_[idx] == s_[idx - 1]:
                continue
            track.append(ch)
            back_pack(s_[:idx] + s_[idx + 1:], track)
            track.pop()

    # 先进行排序
    s = list(sorted(s))
    back_pack(s, [])
    return result_list


print(permutation('aabc'))


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


# https://leetcode-cn.com/problems/combination-sum/
def combine_sum(candidates, target):
    if not candidates:
        return []

    res, _track = list(), list()

    def back_track(track):
        if sum(track) == target:
            temp = track.copy()
            temp.sort()
            if temp not in res:
                res.append(temp)
            return

        # 保证当和大于 target 的时候需要退出，避免无线循环
        if sum(track) > target:
            return

        for item in candidates:
            track.append(item)
            back_track(track)
            track.pop()

    size = len(candidates)

    # 使用 start 来标记，避免一些组合的重复遍历
    def backtrack(start, track, _target):
        # if _target == 0:
        #     res.append(track.copy())
        #     return
        if sum(track) == target:
            res.append(list(track))
            return
        for i in range(start, size):
            if candidates[i] > _target:
                continue
            track.append(candidates[i])
            backtrack(i, track, _target - candidates[i])
            track.pop()

    # back_track(_track)
    backtrack(0, _track, target)
    return res


print('combine_sum is ', combine_sum([8, 7, 4, 3], 11))


# https://leetcode-cn.com/problems/combination-sum-ii/submissions/
# 以下链接解释了为什么能避免重复
# https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/
def combine_sum_ii(candidates, target):
    size = len(candidates)
    if size == 0:
        return []

    # 会出现重复元素的情况下都先排序
    candidates.sort()
    res = list()

    def back_track(start, track, _target):
        if _target == 0:
            res.append(track.copy())
            return

        for i in range(start, size):
            # 当前处理的值已经大于 target，跳过不做处理
            if candidates[i] > _target:
                break

            # 避免重复处理
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            track.append(candidates[i])
            back_track(i + 1, track, _target - candidates[i])
            track.pop()

    back_track(0, [], target)
    return res


print(combine_sum_ii([8, 7, 4, 3], 11))


# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
def letter_combinations(digits):
    if not digits:
        return []

    size = len(digits)
    res, _track = list(), list()

    digit_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def back_track(idx, track):
        if len(_track) == size:
            res.append(''.join(track))
            return

        for ch in digit_map.get(digits[idx]):
            _track.append(ch)
            back_track(idx+1, track)
            track.pop()
        return

    back_track(0, _track)
    return res


_digits = '23'
print(f'letter_combinations for "{_digits}" is {letter_combinations(_digits)}')


# https://leetcode-cn.com/problems/palindrome-partitioning/
# https://leetcode-cn.com/problems/palindrome-partitioning/solution/dong-tai-gui-hua-dfs-by-powcai/
def partition(s):
    if not s:
        return []

    res, _track = list(), list()

    def back_track(_s, track):
        if not _s:
            res.append(track)

        for i in range(1, len(_s)+1):
            if _s[:i] == _s[:i][::-1]:
                back_track(_s[i:], track + [_s[:i]])

    back_track(s, _track)
    return res


print(f'partition of aab is {partition("aab")}')


# 计算子集
# 仅适用于没有重复的情况
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
    nums.sort()

    def back_track(start, track):
        res.append(list(track))

        for i in range(start, len(nums)):
            track.append(nums[i])
            back_track(i + 1, track)
            track.pop()

    back_track(0, [])
    return res


print('subset_backtrack is ', subset_backtrack([1, 2, 3]))


# [4,4,4,1,4]
def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    res = list()
    nums.sort()

    def back_track(start, track):
        # if list(track) not in res:
        res.append(list(track))

        for i in range(start, len(nums)):
            # 去重
            if i > start and nums[i] == nums[i-1]:
                continue
            track.append(nums[i])
            back_track(i + 1, track)
            track.pop()

    back_track(0, [])
    return res


print(subsets_with_dup([4, 4, 4, 1, 4]))


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


# https://leetcode-cn.com/problems/restore-ip-addresses/solution/
# https://github.com/dashidhy/algorithm-pattern-python/blob/master/advanced_algorithm/backtrack.md
def restore_ip_addresses(s):
    size = len(s)
    res, _track = list(), list()

    if size > 12:
        return res

    def valid_s(i, j):
        return i < j <= size and ((s[i] != '0' and int(s[i:j]) < 256) or s[i] == '0' and i == j-1)

    def back_track(start, track):
        if len(track) == 3:
            if valid_s(start, size):
                res.append('.'.join(track) + '.' + s[start:])
            return

        for i in range(start, size):
            if valid_s(start, i+1):
                track.append(s[start:i+1])
                back_track(i + 1, track)
                track.pop()
        return

    back_track(0, _track)
    return res


print(restore_ip_addresses('25525511135'))
