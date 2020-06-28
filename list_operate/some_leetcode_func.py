import bisect
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
