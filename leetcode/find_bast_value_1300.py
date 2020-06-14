"""
leetcode 1300
主要思想 左边界的微分查找和前缀和
"""
from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        nums = sorted(arr)
        size = len(nums)

        left, right = 0, size - 1
        min_index = 0
        while left <= right:
            index = int(left + (right - left) / 2)
            temp_target = target - sum(nums[:index])
            temp_count = size - index
            # 找到正好等于 temp_target 的值，或者 index - 1 是小于，但是 index 是大于的情况就退出 while
            if nums[index] * temp_count > temp_target:
                # 大于的时候向左移动
                if nums[index - 1] * temp_count < temp_target - nums[index]:
                    min_index = index - 1
                    break
                right = index - 1
            elif nums[index] * temp_count < temp_target:
                # 小于的时候向右移动
                if index + 1 < size and nums[index + 1] * temp_count > temp_target + nums[index]:
                    min_index = index
                    break
                left = index + 1
            else:
                return nums[index]

        if min_index + 1 > size:
            return nums[min_index]

        if min_index == 0 and nums[min_index] * size > target:
            # 最小值都大于 target 的情况
            return self.helper(0, nums[0], size, target)

        return self.helper(nums[min_index], nums[min_index + 1], size, target)

    @staticmethod
    def helper(min_num, max_num, size, target):
        # 二分查找
        import math
        left, right = min_num, max_num - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if mid * size < target:
                left = mid + 1
            elif mid * size > target:
                right = mid - 1
            else:
                return mid
        # 找到 abs 更小的一个
        return left if math.fabs(target - size * left) < math.fabs(target - size * right) else right


_arr = [1547, 83230, 57084, 93444, 70879]
_target = 71237
print(Solution().findBestValue(_arr, _target))


# 17422


# 官方解法
class Solution1:
    def findBestValue(self, arr: List[int], target: int) -> int:
        import bisect
        arr.sort()
        n = len(arr)
        prefix = [0]
        # 计算前缀和
        for num in arr:
            prefix.append(prefix[-1] + num)

        # 二分查找，最小值为 0，最大值为 max(arr)
        l, r, ans = 0, max(arr), -1
        # 二分查找找出左边界
        while l <= r:
            mid = (l + r) // 2
            it = bisect.bisect_left(arr, mid)
            cur = prefix[it] + (n - it) * mid
            if cur <= target:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        def check(x):
            return sum(x if num >= x else num for num in arr)

        choose_small = check(ans)
        choose_big = check(ans + 1)
        return ans if abs(choose_small - target) <= abs(choose_big - target) else ans + 1
