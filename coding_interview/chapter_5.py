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
    for n in range(1, num+1):
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
        if i < j <= size and 0 <= int(_num[i:j]) < 26:
            if len(_num[i:j]) >= 2 and _num[i:j].startswith('0'):
                return False
            return True

    def back_track(start, track):
        if start == size:
            result.append(track.copy())
            return

        for i in range(start, size):
            if is_valid(start, i+1):
                track.append(_num[start:i+1])
                back_track(i+1, track)
                track.pop()
        return
    back_track(0, [])
    return result


print(translate_num(12258))
print(translate_num(648006092))


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

    # 因为 do[i] 的值只与 i-2 和 i-1 相关，所以只需要保存两个变量即可，类似于 fib
    a = b = 1
    for i in range(2, len(s) + 1):
        a, b = (a+b if '10' <= s[i-2:i] <= '25' else a), a
    return a


print(translate_num_dp(12258))
print(translate_num_dp(648006092))