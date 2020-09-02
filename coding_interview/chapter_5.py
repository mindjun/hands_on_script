from typing import List


# https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/mian-shi-ti-39-shu-zu-zhong-chu-xian-ci-shu-chao-3/
def majority_element(nums):
    votes, count = 0, 0
    x = nums[0]
    for num in nums:
        if votes == 0:
            x = num
        votes += 1 if num == x else -1
    for num in nums:
        if num == x:
            count += 1
    return x if count > len(nums) // 2 else 0


# https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
def get_least_numbers(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return []

    import heapq
    # heapq 默认是小顶堆
    # 只有大于该堆顶的元素才会加入堆，所以堆中维护的时前 k 大的元素，所以求最小的 k 个数时，取负值即可
    hp = [-x for x in arr[:k]]
    heapq.heapify(hp)

    for i in range(k, len(arr)):
        if -hp[0] > arr[i]:
            heapq.heapreplace(hp, -arr[i])
    return [-x for x in hp]


# https://leetcode-cn.com/problems/maximum-subarray/
def max_sub_array_dp(nums: List[int]) -> int:
    dp = [nums[0] for _ in nums]
    length = len(nums)
    result = dp[0]

    for i in range(1, length):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        result = max(result, dp[i])

        return result


def max_sub_array(nums: List[int]) -> int:
    if not nums:
        return 0

    max_now = nums[0]
    temp_list = [nums[0]]

    for i in nums[1:]:
        if temp_list[-1] > 0:
            temp_item = temp_list[-1] + i
            temp_list.append(temp_item)
            max_now = max(max_now, temp_item)
        else:
            temp_list.append(i)
            max_now = max(max_now, i)
    return max_now


print(max_sub_array([-1]))


# 计算 1 至 n 中数字 x 出现的次数 x in range[1, 10)
# https://www.cnblogs.com/cyjb/p/digitOccurrenceInRegion.html
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
        if k == 0:
            break
    return cnt


print(count(12, 1))
print(f'2593 中 5 出现 {count(2593, 5)} 次')


# 计算 1 至 n 中数字 x 出现的次数 x in range[0, 10)
# 统计包括 0 出现次数的情况
# https://www.cnblogs.com/cyjb/p/digitOccurrenceInRegion.html
def count_include_0(n, x):
    cnt, k, i = 0, n, 1
    while True:
        high = k // 10
        cur = k % 10

        if x == 0:
            if high:
                high -= 1
            else:
                break

        cnt += high * i

        if cur > x:
            cnt += i
        elif cur == x:
            # 2500 -- 2593 ==> 94
            cnt += n % i + 1
        i *= 10
        k = int(n / i)
        if k == 0:
            break
    return cnt


print(f'1-12 中 1 出现 {count_include_0(12, 1)} 次')
print(f'1-2593 中 5 出现 {count_include_0(2593, 5)} 次')


def test_n(num, k):
    # 常规方法用来比较
    ret = 0
    for n in range(1, num + 1):
        for s in str(n):
            if s == str(k):
                ret += 1
    return ret


# 仅计算 1-n 中 1 出现的次数
# https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/mian-shi-ti-43-1n-zheng-shu-zhong-1-chu-xian-de-2/
def count_digit_one(n):
    digit, res = 1, 0
    high, low, cur = n // 10, 0, n % 10

    while high != 0 or cur != 0:
        if cur == 0:
            res += high * digit
        elif cur == 1:
            res += high * digit + low + 1
        else:
            res += (high + 1) * digit
        low += cur * digit
        cur = high % 10
        high = high // 10
        digit *= 10
    return res


print(count_digit_one(12))


# https://leetcode-cn.com/problems/nth-digit/
def find_nth_digit(n: int) -> int:
    if n < 10:
        return n

    n -= 10
    start, index = 10, 2
    while True:
        now_count = 9 * start * index
        if n <= now_count:
            break

        n -= now_count
        index += 1
        start *= 10
    # num_index 代表 index 位数的 num_index 个
    num_index = n // index
    # num_location 代表 index 位数的 num_location 位
    num_location = n % index
    return int(str(start + num_index)[num_location])


print(find_nth_digit(1001))


# https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
# 回溯的方法解决
def translate_num(num):
    _num = str(num)
    size = len(_num)
    result = list()

    def is_valid(i, j):
        return i < j <= size and 0 <= int(_num[i:j]) < 26

    def back_track(start, track):
        if start == size:
            result.append(track.copy())

        for i in range(start, size):
            if is_valid(start, i + 1):
                if len(_num[start:i + 1]) >= 2 and _num[start:i + 1].startswith('0'):
                    continue
                track.append(_num[start:i + 1])
                back_track(i + 1, track)
                track.pop()
        return

    back_track(0, [])
    return len(result)


print(f'translate_num 12258 is {translate_num(12258)}')
print(f'translate_num 648006092 is {translate_num(648006092)}')


# https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/mian-shi-ti-46-ba-shu-zi-fan-yi-cheng-zi-fu-chua-6/
# dp[i] 代表以 num[i] 为结尾的数字的翻译方案数量，即 num[i] 结尾的字符的翻译方案数量
# 若 num[i] 和 num[i-1] 组成的两位数字可以被翻译，dp[i] = dp[i-1] + dp[i-2]，否则 dp[i] = dp[i-1]
def translate_num_dp(num):
    s = str(num)

    # dp = [0] * (len(s) + 1)
    # dp[0] = dp[1] = 1
    #
    # for i in range(2, len(s) + 1):
    #     if '10' <= s[i-2:i] <= '25':
    #         dp[i] = dp[i-1] + dp[i-2]
    #     else:
    #         dp[i] = dp[i-1]
    # return dp[-1]

    # 因为 dp[i] 的值只与 i-2 和 i-1 相关，所以只需要保存两个变量即可，类似于 fib
    a = b = 1
    for i in range(2, len(s) + 1):
        a, b = (a + b if '10' <= s[i - 2:i] <= '25' else a), a
    return a


print(f'translate_num_dp 12258 is {translate_num_dp(12258)}')
print(f'translate_num_dp 648006092 is {translate_num_dp(648006092)}')


# https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/solution/mian-shi-ti-47-li-wu-de-zui-da-jie-zhi-dong-tai-gu/
# 空间优化，直接在 grid 上进行修改
def max_value(grid):
    # 初始化第一行和第一列
    for j in range(1, len(grid)):
        grid[0][j] += grid[0][j - 1]

    for i in range(1, len(grid[0])):
        grid[i][0] += grid[i - 1][0]

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
    return grid[-1][-1]


# https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
def length_of_longest_substring(s):
    if not s:
        return 0
    from collections import defaultdict
    windows = defaultdict(int)
    max_len, left, right = 0, 0, 0

    while right < len(s):
        ch = s[right]
        right += 1
        windows[ch] += 1

        while windows[ch] > 1:
            ch2 = s[left]
            windows[ch2] -= 1
            left += 1

        if windows[ch] == 1:
            max_len = max(max_len, right - left)
    return max_len


# https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/solution/mian-shi-ti-48-zui-chang-bu-han-zhong-fu-zi-fu-d-9/
def length_of_longest_substring_ii(s):
    dic = dict()
    res = tmp = 0
    for j in range(len(s)):
        i = dic.get(s[j], -1)
        dic[s[j]] = j

        if tmp < j - i:
            tmp += 1
        else:
            tmp = j - i
        res = max(res, tmp)
    return res


# https://leetcode-cn.com/problems/chou-shu-lcof/solution/mian-shi-ti-49-chou-shu-dong-tai-gui-hua-qing-xi-t/
def nth_ugly_number(n):
    dp = [1] * n
    a, b, c = 0, 0, 0
    for i in range(1, n):
        n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
        dp[i] = min(n2, n3, n5)
        if dp[i] == n2:
            a += 1
        if dp[i] == n3:
            b += 1
        if dp[i] == n5:
            c += 1
    return dp[-1]


print(nth_ugly_number(10))


# https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/

def reverse_pairs(nums):
    _count = 0

    def merge_sort(_nums):
        if len(_nums) <= 1:
            return _nums
        mid = len(_nums) // 2
        left = merge_sort(_nums[:mid])
        right = merge_sort(_nums[mid:])
        return merge(left, right)

    def merge(left, right):
        size_left, size_right = len(left), len(right)
        result = [-1] * (size_left + size_right)
        result_index = len(result) - 1
        nonlocal _count
        while left and right:
            if left[-1] > right[-1]:
                _count += len(right)
                result[result_index] = left.pop()
            else:
                result[result_index] = right.pop()
            result_index -= 1

        index = 0
        for x, _ in zip(left or right, result):
            result[index] = x
            index += 1
        return result

    print(merge_sort(nums))
    return _count


print(reverse_pairs([7, 5, 6, 4]))


# https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/solution/mian-shi-ti-53-ii-0n-1zhong-que-shi-de-shu-zi-er-f/
def missing_number(nums):
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) >> 1
        if nums[m] == m:
            i = m + 1
        else:
            j = m - 1
    # 变量 i 和 j 分别指向 “右子数组的首位元素” 和 “左子数组的末位元素”
    return i


print(missing_number([0, 1, 3]))


# https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-by-leetcode/
# 只出现一次的数字
def single_numbers(nums):
    ret = 0
    for num in nums:
        ret ^= num

    div = 1
    while div & ret == 0:
        div <<= 1
    a, b = 0, 0
    for num in nums:
        if num & div:
            a ^= num
        else:
            b ^= num
    return [a, b]


print(single_numbers([2, 4, 3, 6, 3, 2, 5, 5]))


# https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
def find_continuous_sequence(target):
    if target < 3:
        return []

    small, big, result = 1, 2, list()
    middle = (1 + target) >> 1
    cur_sum = small + big
    while small < middle:
        if cur_sum == target:
            result.append(list(range(small, big + 1)))
        while cur_sum > target and small < middle:
            cur_sum -= small
            small += 1
            if cur_sum == target:
                result.append(list(range(small, big + 1)))
        big += 1
        cur_sum += big
    return result


print(find_continuous_sequence(9))


# https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/
def reverse_words(s):
    temp_list = s.split(' ')[::-1]
    return ' '.join(temp_list)


print(reverse_words("the sky is blue"))


# https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/solution/mian-shi-ti-61-bu-ke-pai-zhong-de-shun-zi-ji-he-se/
def is_straight(nums):
    joker = 0
    nums.sort()

    for i in range(4):
        if nums[i] == 0:
            joker += 1
        elif nums[i] == nums[i + 1]:
            return False
    return nums[-1] - nums[joker] < 5


class LinkedNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return f'{self.val}'


# https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/
def last_remaining(n, m):
    if n == 1:
        return 0
    # 生成一个唤醒链表
    node_list = [LinkedNode(v) for v in range(n)]
    for index, node in enumerate(node_list):
        if index == n - 1:
            node.set_next(node_list[0])
        else:
            node.set_next(node_list[index + 1])

    result = list()
    head = node_list[0]
    while len(result) < n - 1:
        k = 1
        # k 设置为 m-1 的位置，方便链表删除下一个节点
        while k < m - 1:
            head = head.next
            k += 1
        result.append(head.next.val)
        head.next = head.next.next
        head = head.next
    print(result)
    return head.val


print(last_remaining(10, 17))


# 约瑟夫环解决
# 设 f(n, m) = x 表示长度为 n，数 m 个元素之后留下的元素为 x
# f(n, m) = (f(n-1, m) + m) % n
def last_remaining_ii(n, m):
    if n < 1 or m < 1:
        return -1

    last = 0
    for i in range(2, n + 1):
        last = (last + m) % i
    return last


print(last_remaining_ii(10, 17))


def max_profit(prices):
    cost, profit = float('inf'), 0
    for price in prices:
        cost = min(cost, price)
        profit = max(profit, price - cost)
    return profit


print(max_profit([7, 1, 5, 3, 6, 4]))