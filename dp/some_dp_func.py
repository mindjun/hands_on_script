from typing import List
from collections import defaultdict


# https://leetcode-cn.com/problems/triangle/
# dfs 解法，leetcode 超过时间限制
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
def minimum_total(triangle):
    min_sum = float('inf')
    path = list()
    result = list()

    def dfs(start_x, start_y, temp_res):
        if start_x == len(triangle) - 1:
            nonlocal min_sum
            min_sum = min(min_sum, temp_res + triangle[start_x][start_y])
            result.append(list(path))
            return

        path.append([start_x + 1, start_y])
        dfs(start_x + 1, start_y, temp_res + triangle[start_x][start_y])
        path.pop()

        path.append([start_x + 1, start_y + 1])
        dfs(start_x + 1, start_y + 1, temp_res + triangle[start_x][start_y])
        path.pop()

    dfs(0, 0, 0)
    print(result)
    for path_ in result:
        _temp_res = triangle[0][0]
        _path = f'{_temp_res}'
        for item in path_:
            _temp_res += triangle[item[0]][item[1]]
            _path += f' ==> {triangle[item[0]][item[1]]}'
        print(f'path {_path} sum is {_temp_res}')
    return min_sum


# 自顶向下
# 结果为 dp 最后一列中的最小值
def minimum_total_dp_top_down(triangle):
    dp = [[0] * len(triangle[i]) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 分为上一层没有左边值，没有右边值，正常的三种情况
            if j - 1 < 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j >= len(triangle[i]) - 1:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

    print(f'minimum_total_dp is {dp}')
    return min(dp[-1])


# 自底向上
def minimum_total_with_cache(triangle):
    cache = [[-1] * len(triangle[i]) for i in range(len(triangle))]

    def dfs(x, y):
        if x == len(triangle):
            return 0

        if cache[x][y] != -1:
            return cache[x][y]
        cache[x][y] = min(dfs(x + 1, y), dfs(x + 1, y + 1)) + triangle[x][y]
        return cache[x][y]

    res = dfs(0, 0)
    print(cache)
    return res


# 自底向上，与 cache 版本一致，先将 dp[-1] 这一行初始化为 triangle 的最后一行，我们要求的结果就在 dp[0][0]
# dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
def minimum_total_dp(triangle):
    dp = [[0] * len(triangle[i]) for i in range(len(triangle))]
    for index, item in enumerate(triangle[-1]):
        dp[-1][index] = item

    for i in range(len(triangle) - 1)[::-1]:
        for j in range(len(triangle[i])):
            dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
    print(f'minimum_total_dp is {dp}')
    return dp[0][0]


triangle_ = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
triangle__ = [
    [1],
    [-2, -5],
    [3, 6, 9],
    [-1, 2, 4, -3]]
print(minimum_total(triangle__))
print(minimum_total_with_cache(triangle__))
print(minimum_total_dp(triangle__))
print(minimum_total_dp_top_down(triangle__))


# https://leetcode-cn.com/problems/minimum-path-sum/
# 自底向上
def min_path_sum_cache(nums):
    cache = [[-1] * (len(nums[0]) + 1) for _ in range(len(nums) + 1)]

    def dfs(x, y):
        if x == len(nums) - 1 and y == len(nums[-1]) - 1:
            return nums[-1][-1]

        # x 到达最下边，只能移动 y
        if x == len(nums) - 1:
            cache[x][y] = dfs(x, y + 1) + nums[x][y]
            return cache[x][y]
        # y 到达最右边，只能移动 x
        if y == len(nums[x]) - 1:
            cache[x][y] = dfs(x + 1, y) + nums[x][y]
            return cache[x][y]

        if cache[x][y] != -1:
            return cache[x][y]

        cache[x][y] = min(dfs(x + 1, y), dfs(x, y + 1)) + nums[x][y]
        return cache[x][y]

    # 从 (0, 0) 的位置开始遍历
    res = dfs(0, 0)
    print(cache)
    return res


print(min_path_sum_cache([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))


# 自顶向下，需要考虑下标越界的情况
def min_path_sum_dp(nums):
    dp = [[-1] * len(nums[0]) for _ in nums]
    dp[0][0] = nums[0][0]

    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if i == 0 and j == 0:
                continue
            if i == 0:
                dp[i][j] = dp[i][j - 1] + nums[i][j]
                continue
            if j == 0:
                dp[i][j] = dp[i - 1][j] + nums[i][j]
                continue
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + nums[i][j]
    return dp[-1][-1]


path_ = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(min_path_sum_dp(path_))


# https://leetcode-cn.com/problems/unique-paths/
# 回溯的方法，顺便能拿到路径
def unique_paths_dfs(m, n):
    path_count = 0
    path_list = list()

    def dfs(x, y, path):
        if x == m or y == n:
            return

        if x == m - 1 and y == n - 1:
            nonlocal path_count
            path_count += 1
            path_list.append(path.copy())
            return

        path.append((x, y))
        dfs(x + 1, y, path)
        path.pop()

        path.append((x, y))
        dfs(x, y + 1, path)
        path.pop()

    dfs(0, 0, [])
    for _path in path_list:
        path_str = ''
        for sub_path in _path:
            path_str += f'{sub_path} ==> '
        path_str = path_str + f'{(m - 1, n - 1)}'
        print(path_str)
    return path_count


print(unique_paths_dfs(3, 7))


def unique_paths_dp(m, n):
    dp = [[1] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if j == 0:
                dp[i][j] = dp[i - 1][j]
                continue
            if i == 0:
                dp[i][j] = dp[i][j - 1]
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


print(unique_paths_dp(3, 7))


# 这里涉及到滚动数组的概念
# 可以理解为每次求解一行的解，每一列的值只与前一行相关
# 下一列的值也只与前一行和前一列相关，而前一行的值已经暂存在数组中，所以只需要取前一列的值
def unique_paths_dp_(m, n):
    if n < m:
        n, m = m, n
    dp = [1] * m
    for i in range(1, n):
        for j in range(1, m):
            dp[j] += dp[j - 1]
    return dp[-1]


print(unique_paths_dp_(3, 7))


# https://leetcode-cn.com/problems/unique-paths-ii/
def unique_paths_dp_ii(matrix_):
    if not matrix_:
        return 0

    n, m = len(matrix_), len(matrix_[0])
    dp = [0] * m
    if matrix_[0][0] == 0:
        dp[0] = 1

    for i in range(n):
        for j in range(m):
            if matrix_[i][j] == 1:
                dp[j] = 0
                continue
            if j - 1 > 0 and matrix_[i][j] == 0:
                dp[j] += dp[j - 1]
    return dp[-1]


# https://leetcode-cn.com/problems/jump-game/
def can_jump(nums):
    farthest, size = 0, len(nums)
    for i in range(size):
        farthest = max(farthest, i + nums[i])
        if farthest >= size - 1:
            return True
        if farthest <= i:
            return False
    return farthest >= size - 1


# tail to head
def can_jump_dp(nums):
    # 从后往前依次判断，当前的 left + i 是否能
    left = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        left = i if i + left >= left else left
    return left == 0


print(can_jump([3, 2, 1, 0, 4]))


# https://leetcode-cn.com/problems/jump-game-ii/
def jump(nums):
    dp = [1] * len(nums)
    dp[0] = 0
    for i in range(1, len(nums)):
        temp_list = [dp[i - j] for j in range(nums[i]) if i - j >= 0]
        print(f'now temp_list is {temp_list}, now i is {i}')
        dp[i] = min(temp_list) + 1
    return dp[-1]


print(jump([2, 3, 1, 1, 4]))


# https://leetcode-cn.com/problems/jump-game-ii/
# 从后往前，每次都找到能到达当前位置的点，并跳到改点
# 贪心算法
def jump_ii(nums):
    size, step = len(nums), 0
    position = size - 1

    while position > 0:
        # 我们可以从左到右遍历数组，选择第一个满足要求的位置
        for i in range(position):
            if i + nums[i] >= position:
                position = i
                step += 1
                break
    return step


print(jump_ii([2, 3, 1, 1, 4]))


# 贪心算法
# 从前往后，每次都取当前节点能到达的最大位置
# 我们维护当前能够到达的最大下标位置，记为边界。我们从左到右遍历数组，到达边界时，更新边界并将跳跃次数增加 1
def jump_ii_(nums):
    step = end = max_position = 0
    size = len(nums)
    for i in range(size - 1):
        if max_position >= i:
            max_position = max(max_position, i + nums[i])

            if i == end:
                end = max_position
                step += 1
    return step


# https://leetcode-cn.com/problems/palindrome-partitioning-ii/
# https://leetcode-cn.com/problems/palindrome-partitioning-ii/solution/dong-tai-gui-hua-hui-su-zhu-xing-jie-shi-python3-b/
def min_cut(s):
    size = len(s)
    # 长度为 n 的字符串最少分割的次数为 min_list[n]
    min_list = list(range(size))

    # dp[i][j] 代表 s[i..j] 是否为回文
    dp = [[False] * size for _ in range(size)]
    # 循环 i [0..size] 和 j [i..size+1]
    for j in range(size):
        for i in range(j + 1):
            # i..j 为回文的条件为 s[i] == s[j] 并且 (i+1 ... j-1 是回文 或者 i..j 的长度为 1)
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                # 若 i==0，开始位置为 0，说明s[0...j] s[0...j]为回文串，
                # 则此时 min_cut[j]=0，表示到 j 位置的子串不需要进行切割，自身就是回文子串
                if i == 0:
                    min_list[j] = 0
                else:
                    # 始终为到上一回文串位置的切割次数加1中的最小值
                    min_list[j] = min(min_list[j], min_list[i - 1] + 1)
    return min_list[-1]


# https://leetcode-cn.com/problems/longest-increasing-subsequence/
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


# https://leetcode-cn.com/problems/russian-doll-envelopes/
# 俄罗斯套娃信封问题
# 本质上就是在 envelopes 按照 w 升序，h 降序之后的 h 所在的序列查找最长上升子序列
def max_envelopes(envelopes: List[List[int]]) -> int:
    if not envelopes:
        return 0

    # 动态规划查找最长上升子序列
    # nums = sorted(envelopes, key=lambda x: (x[0], -x[1]))
    # heights = [i[1] for i in nums]
    #
    # dp = [1] * len(heights)
    # for i in range(len(heights)):
    #     for j in range(0, i):
    #         if heights[i] > heights[j]:
    #             dp[i] = max(dp[i], dp[j] + 1)
    # return max(dp)

    import bisect
    subset = []
    # 二分查找的方式查找最长上升子序列
    for env in sorted(envelopes, key=lambda x: (x[0], -x[1])):
        pos = bisect.bisect_left(subset, env[1])
        if pos == len(subset):
            subset.append(env[1])
        elif env[1] < subset[pos]:
            subset[pos] = env[1]
    return len(subset)


print(f'max_envelopes is {max_envelopes([[5, 4], [6, 4], [6, 7], [2, 3]])}')


# https://leetcode-cn.com/problems/word-break/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 带缓存的回溯方法
        # import functools
        # @functools.lru_cache(None)
        # def back_track(s):
        #     if not s:
        #         return True
        #     res = False
        #     for i in range(1, len(s) + 1):
        #         if s[:i] in wordDict:
        #             res = back_track(s[i:]) or res
        #     return res
        #
        # return back_track(s)

        n = len(s)
        # 初始化为 False
        dp = [False] * (n + 1)
        # 空字符串可以被表示
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                # 如果前 i 个字符可以被 wordDict 表示，并且 [i...j] 可以被 wordDict 表示，那么前 j 个字符也可以被表示
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]


def word_break(s, word_dict):
    import functools

    @functools.lru_cache(None)
    def back_track(_s):
        if not _s:
            return True
        res = False
        for i in range(1, len(_s) + 1):
            if _s[:i] in word_dict:
                res = back_track(_s[i:]) or res
        return res

    return back_track(s)


# 最长公共子序列
# https://leetcode-cn.com/problems/longest-common-subsequence/
def longest_common_sub_sequence(text1: str, text2: str) -> int:
    len1, len2 = len(text1), len(text2)
    # 需要考虑字符串为空的时候，所以 dp 的长度都需要为 size + 1, 并且 dp[i][0] = 0
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
    # dp[i][j] 为 text1[:i] 与 text2[:j] 的最长公共子序列
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


# 最短编辑距离
# https://leetcode-cn.com/problems/edit-distance/
# dp[i][j] = min(dp[i-1][j-1], dp[i-1][j] + 1, dp[i][j-1] + 1)
def edit_distance(str1, str2):
    size1, size2 = len(str1), len(str2)
    # 需要考虑字符串为空，所以 dp 的长度需要 size + 1
    dp = [[(size1 + size2) for _ in range(size2 + 1)] for _ in range(size1 + 1)]

    # 初始化 dp[i][0] = 0
    for i in range(size1 + 1):
        dp[i][0] = i
    # 初始化 dp[0][j] = 0
    for j in range(size2 + 1):
        dp[0][j] = j

    # print(dp)

    for i in range(1, size1 + 1):
        for j in range(1, size2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    # print(dp)
    return dp[-1][-1]


# abcd->eebcc
print(edit_distance('abcd', 'eebcc'))


# https://leetcode-cn.com/problems/coin-change/
def coin_change(coins, amount):
    dp = [amount + 1 for _ in range(amount + 1)]
    # 一定要初始化 dp[0] = 0
    dp[0] = 0
    result = defaultdict(list)
    for n in range(0, amount + 1):
        for coin in coins:
            # coin
            if n - coin < 0:
                continue
            # dp[n] = min(dp[n], 1 + dp[n - coin])
            if dp[n] < 1 + dp[n - coin]:
                continue
            else:
                dp[n] = 1 + dp[n - coin]
                result[n].append(coin)
    return dp[-1], result


print('coin_change ', coin_change([1, 2, 5], 11))


def coin_change_(coins, amount):
    dp = [amount + 1] * (amount + 1)
    # 一定要初始化 dp[0] = 0
    dp[0] = 0

    for i in range(0, amount + 1):
        for coin in coins:
            if i - coin < 0:
                continue
            dp[i] = min(dp[i], 1 + dp[i - coin])

    return -1 if dp[-1] == amount + 1 else dp[-1]


print('coin_change ', coin_change_([2], 3))


def coin_change__(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    # 以 coin 为出发点
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[-1] == amount + 1:
        return -1
    return dp[-1]


# https://leetcode-cn.com/problems/coin-change-2/
# 零钱兑换 II, 求能凑足目标金额的方案次数
# 可以理解为完全背包问题
def coin_change_ii(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = dp[i] + dp[i-coin]
    return dp[-1]


# https://leetcode-cn.com/problems/maximum-product-subarray/
def max_product(nums):
    dp_max = [float('-inf')] * (len(nums) + 1)
    dp_min = [float('inf')] * (len(nums) + 1)
    dp_max[0] = 1
    dp_min[0] = 1

    for index, item in enumerate(nums, 1):
        dp_max[index] = max(item, dp_max[index - 1] * item, dp_min[index - 1] * item)
        dp_min[index] = min(item, dp_max[index - 1] * item, dp_min[index - 1] * item)
    return max(dp_max[1:])


print(max_product([-2, 3, -4]))


# 滚动数组的空间优化
# 第 i、个状态只和第 i-1 个状态有关
def max_product_ii(nums):
    max_f, min_f, res = nums[0], nums[0], nums[0]
    for item in nums[1:]:
        # 使用临时变量保存上一次的计算结果
        temp_max, temp_min = max_f, min_f
        max_f = max(temp_max * item, temp_min * item, item)
        min_f = min(temp_max * item, temp_min * item, item)
        res = max(max_f, res)
    return res


print(max_product_ii([-4, -3, -2]))


# https://leetcode-cn.com/problems/decode-ways/solution/dong-tai-gui-hua-by-chuan-12/
# 设数字串S的前i个数字解密成字母串有dp[i]种方式：那么就有dp[i] = dp[i-1] + dp[i-2]
def num_decoding(s):
    if not s:
        return 0

    dp = [0] * (len(s) + 1)
    dp[0] = 1

    for i in range(1, len(s) + 1):
        t = int(s[i - 1])
        if 1 <= t <= 9:
            dp[i] += dp[i - 1]
        if i >= 2:
            t = int(s[i - 2]) * 10 + int(s[i - 1])
            if 9 < t < 27:
                dp[i] += dp[i - 2]
    return dp[-1]


print(num_decoding('226'))


# 空间优化，因为 dp[i] 的状态只与 i-1 和 i-2 有关，所以只需要保存前面的两个状态
def num_decoding_ii(s):
    if not s:
        return 0

    def valid_2(index):
        if index < 1:
            return 0
        num = int(s[index - 1:index + 1])
        return int(9 < num < 27)

    dp_1, dp_2 = 1, 0
    for i in range(len(s)):
        dp_1, dp_2 = dp_1 * int(s[i] != '0') + dp_2 * valid_2(i), dp_1

    return dp_1


print(num_decoding_ii('226'))


# https://leetcode-cn.com/problems/longest-palindromic-substring/
# 最长回文子串
def longest_palindrome(s: str) -> str:
    n = len(s)
    # dp[i][j] 代表字符串 i...j 为回文
    # 递推公式为: dp[i][i] = True, dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
    dp = [[False] * n for _ in range(n)]
    ans = ""
    # 枚举子串的长度 l+1
    for l in range(n):
        # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
        for i in range(n):
            j = i + l
            if j >= len(s):
                break
            if l == 0:
                dp[i][j] = True
            elif l == 1:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
            if dp[i][j] and l + 1 > len(ans):
                ans = s[i:j+1]
    return ans


# 最长回文子串
# https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/
def longest_palindrome_dp(s: str) -> str:
    size = len(s)
    if size < 2:
        return s

    dp = [[False for _ in range(size)] for _ in range(size)]

    max_len = 1
    start = 0

    for i in range(size):
        dp[i][i] = True

    for j in range(1, size):
        for i in range(0, j):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False

            if dp[i][j]:
                cur_len = j - i + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = i
    return s[start:start + max_len]


print(longest_palindrome("babad"))

