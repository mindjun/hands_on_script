import random
import bisect
import heapq
from typing import List


# https://leetcode-cn.com/problems/container-with-most-water/
def max_area(height):
    area = 0
    left, right = 0, len(height) - 1

    while left < right:
        now_area = min(height[left], height[right]) * (right - left)
        area = now_area if now_area > area else area

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return area


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))


# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
def remove_duplicates(nums):
    size = len(nums)
    # 没有重复项
    if size == len(set(nums)):
        return size

    left = 0
    for right in range(size):
        # 找到 left 之后第一个不相等的数，并交换不相等的数与 left + 1 下标
        # left 所在的位置就是没有重复数字的最后一个下标
        if nums[left] != nums[right]:
            left += 1
            nums[left], nums[right] = nums[right], nums[left]
    print(f'remove_duplicates num is {nums}')
    return left + 1


print(remove_duplicates([1, 2, 2, 3, 4, 5, 5, 6, 6]))


# https://leetcode-cn.com/problems/move-zeroes/
def move_zero(nums):
    # left, right = 0, len(nums) - 1
    # while left < right:
    #     if nums[left] == 0:
    #         nums[left], nums[left + 1] = nums[left + 1], nums[left]
    #
    #     left += 1
    # return nums

    # left, right = 0, len(nums) - 1
    # while left < right:
    #     if nums[left] == 0:
    #         zero_index = left
    #         while zero_index < right:
    #             # 遇到一个零就将这个零移动到最后，同时 right -= 1
    #             nums[zero_index], nums[zero_index + 1] = nums[zero_index + 1], nums[zero_index]
    #             zero_index += 1
    #         right -= 1
    #     left += 1
    # return nums

    # zero_index = list()
    # index = len(nums) - 1
    # for item in nums[::-1]:
    #     if item == 0:
    #         nums.pop(index)
    #         zero_index.append(index)
    #     index -= 1
    #
    # for _ in zero_index:
    #     nums.append(0)
    # return nums

    # zero_index, has_zero = 0, False
    # for i in range(len(nums)):
    #     # 找到第一个不为 0 的下标，如果之前的元素出现了 0，那么交换
    #     # zero_index 总是小于等于 i
    #     if nums[i] != 0:
    #         if has_zero:
    #             nums[zero_index], nums[i] = nums[i], nums[zero_index]
    #         zero_index += 1
    #     else:
    #         has_zero = True
    # return nums

    # 找到最后一个不为 0 的地方，将该 index 之后的元素全部替换为 0
    # last_non_zero = 0
    # for i in range(len(nums)):
    #     if nums[i] != 0:
    #         nums[last_non_zero] = nums[i]
    #         last_non_zero += 1
    #
    # for i in range(last_non_zero, len(nums)):
    #     nums[i] = 0
    # return nums

    # zero 记录出现 0 的下标
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
    return nums


print(move_zero([1, 2, 3, 0, 4, 0, 5, 6, 0, 7, 8]))


# https://leetcode-cn.com/problems/best-sightseeing-pair/
# 输入：[8,1,5,2,6]
# 输出：11
# 解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
# 因为 A[j] - j 的值是固定的，max(A[i] + A[j] + i - j) ==> max(A[i] + i) + max(A[j] - j)
def best_value(nums):
    res = 0
    pre_num = nums[0] + 0
    for i in range(1, len(nums)):
        res = max(res, pre_num + nums[i] - i)
        pre_num = max(pre_num, nums[i] + i)
    return res


print(best_value([8, 1, 5, 2, 6]))


# https://leetcode-cn.com/problems/3sum-closest/
def three_sum_closest(nums, target):
    nums.sort()
    size = len(nums)
    best = float('-inf')

    for i in range(size):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j, k = i + 1, size - 1
        # 降级为二维，用左右双指针进行求解
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == target:
                return target
            elif s > target:
                k -= 1
            # s < target
            else:
                j += 1
            # 更新 best
            if abs(s - target) < abs(best - target):
                best = s
    return best


_nums = [-1, 0, 1, 1, 55]
_target = 3
print(three_sum_closest(_nums, _target))


# https://leetcode-cn.com/problems/minimum-size-subarray-sum/
def min_length(nums, s):
    # left, right, min_len = 0, 0, len(nums) + 1
    # while right < len(nums) + 1:
    #     # 每次都计算 sum 增加了时间复杂度
    #     while sum(nums[left:right]) >= s:
    #         # 因为算 sum 的时候取 [left, right)， 所以这里 right - left 就好，不需要 + 1
    #         min_len = min(min_len, (right - left))
    #         left += 1
    #     right += 1
    # return 0 if min_len == len(nums) + 1 else min_len

    left, right, temp_sum, min_len = 0, 0, 0, len(nums) + 1
    while right < len(nums):
        while temp_sum < s and right < len(nums):
            temp_sum += nums[right]
            right += 1

        while temp_sum >= s and left < len(nums):
            temp_sum -= nums[left]
            left += 1
        # 注意，这里应该是 right - left + 1
        min_len = min(right - left + 1, min_len)

    return 0 if min_len == len(nums) + 1 else min_len


print(min_length([2, 3, 1, 2, 4, 3], 7))


# 官方题解，前缀和 + 二分查找 O(n log n)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        for i in range(1, n + 1):
            target = s + sums[i - 1]
            # 左边界的二分查找
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans


# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
# 快速排序的思想，在快排中，每一次就是将 target 找到他应该在位置，只是这里换成了下标 index
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/partitionfen-er-zhi-zhi-you-xian-dui-lie-java-dai-/
def find_kth_largest(nums, k):
    """
    找到数组中第 k 大的元素
    """
    # 最简单的方法，排序后直接返回
    # return sorted(nums)[-k]

    # target 代表第 target 小的元素，即代表第 k 大的元素
    size = len(nums)
    target = size - k
    right, left = size - 1, 0

    while True:
        index = partition(left, right, nums)
        # 正好在 target 的位置
        if index == target:
            return nums[target]
        elif index < target:
            # 查找 index+1 --> right
            left = index + 1
        else:
            # index > target
            # 查找 left --> index - 1
            right = index - 1


def partition(_left, _right, nums):
    # 随机取一个值，避免 nums 出现正序或者倒序时 O(n^2) 的时间复杂度
    random_index = random.randint(_left, _right)
    nums[random_index], nums[_left] = nums[_left], nums[random_index]

    pivot = nums[_left]

    # j = _left
    # for i in range(_left+1, _right + 1):
    #     # 当 index 为 i 的数小于 pivot 时，交换 j+1 和 i 的数字
    #     # 可以理解为将小于 pivot 的数字移动到 j 下标的左边
    #     # 即找到 pivot 应该在的位置，类似与插入排序
    #     if nums[i] < pivot:
    #         j += 1
    #         nums[i], nums[j] = nums[j], nums[i]
    # nums[_left], nums[j] = nums[j], nums[_left]
    # return j

    # 也可以使用双指针进行数组的分治
    lt = _left + 1
    rt = _right
    while True:
        while lt <= rt and nums[lt] < pivot:
            lt += 1
        while lt <= rt and nums[rt] > pivot:
            rt -= 1

        if lt > rt:
            break
        nums[lt], nums[rt] = nums[rt], nums[lt]
        lt += 1
        rt -= 1
    nums[_left], nums[rt] = nums[rt], nums[_left]
    return rt


# 使用最小堆来求解，维护以为长度为 k 的最小堆，取堆顶的元素即可
def find_kth_largest_with_heap(nums, k):
    temp_list = nums[:k]
    # heapq 默认是小顶堆
    heapq.heapify(temp_list)

    size = len(nums)
    for index in range(k, size):
        top = temp_list[0]
        # 只要 index 元素大于堆顶元素，就进行替换
        if nums[index] > top:
            # heapq.heapreplace(temp_list, nums[index]) ==>  temp_list[0] = nums[index] && heapq.heapify(temp_list)
            heapq.heapreplace(temp_list, nums[index])
    # 最后堆顶的元素就是第 k 大的元素
    return temp_list[0]


print(find_kth_largest_with_heap([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))


# 使用两个栈来实现一个队列
class CQueue(object):
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def append_tail(self, value: int) -> None:
        self.stack1.append(value)

    def delete_head(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return -1


# 暴力解法
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
def find_length(a, b):
    max_length = -1

    for i in range(len(a)):
        for j in range(len(b)):
            offset = 0
            while i + offset < len(a) and j + offset < len(b) and a[i + offset] == b[j + offset]:
                offset += 1
            max_length = max(offset, max_length)
    return max_length


# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode-solution/
class Solution(object):
    def find_length(self, a: List[int], b: List[int]) -> int:
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if a[i] == b[j] else 0
                ans = max(ans, dp[i][j])
        return ans


print(Solution().find_length([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]))


# 滑动窗口，找到相同的位置，并对齐
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode-solution/
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def maxLength(addA: int, addB: int, length: int) -> int:
            ret = k = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret

        n, m = len(A), len(B)
        ret = 0
        for i in range(n):
            length = min(m, n - i)
            ret = max(ret, maxLength(i, 0, length))
        for i in range(m):
            length = min(n, m - i)
            ret = max(ret, maxLength(0, i, length))
        return ret


# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
# 示例：
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# 返回 13。
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/
class Solution(object):
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


_matrix = [
   [1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
_matrix1 = [
   [1, 2],
   [1, 3]
]
print(Solution().kthSmallest(_matrix1, 2))


# https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/
def eval_rpm(tokens: List[str]):
    temp_stack = list()
    for i in tokens:
        if i in '+-*/':
            num1 = temp_stack.pop()
            num2 = temp_stack.pop()
            temp_stack.append(int(eval(f'{num2} {i} {num1}')))
        else:
            temp_stack.append(i)
    return int(temp_stack[0])

    # while True:
    #     if len(tokens) == 1:
    #         return int(tokens[0])
    #     for index, item in enumerate(tokens):
    #         if item in ['+', '-', '*', '/']:
    #             num1 = tokens[index-1]
    #             num2 = tokens[index-2]
    #             tokens[index-2] = str(int(eval(f'{num2} {item} {num1}')))
    #             tokens.pop(index)
    #             tokens.pop(index-1)
    #             break


print(f'eval_rpm res is {eval_rpm(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])}')


# https://leetcode-cn.com/problems/decode-string/
def decode_string(s):
    temp_stack = list()
    for ch in s:
        if ch == ']':
            temp_str = ''
            while temp_stack[-1] != '[':
                temp_str = temp_stack.pop() + temp_str
            # 这时候的最后一个字符一定是 [
            temp_stack.pop()
            repeat_str = ''
            while temp_stack and temp_stack[-1].isnumeric():
                repeat_str = temp_stack.pop() + repeat_str
            repeat_num = int(repeat_str)
            temp_stack.append(repeat_num * temp_str)
        else:
            temp_stack.append(ch)
    return ''.join(temp_stack)


print(f'decode_string is {decode_string("10[leetcode]")}')
assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
