"""
二分查找
"""
# 参考源码的实现
import bisect

print(bisect.bisect_left)
print(bisect.bisect_right)
print(bisect.insort_left)


# 基础模版
def binary_search(nums, target):
    start, end = 0, len(nums) - 1
    # 因为查询的范围是 [start, end]，所以这里是 <=
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1


# 左边界查找
def left_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            # 别返回，锁定左侧边界
            right = mid - 1
    # 最后需要检查左边界的越界情况，并且不一定存在相等的情况
    if left >= len(nums) or nums[left] != target:
        return -1
    return left


# 右边界查找
def right_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            # 别返回，锁定右侧边界
            left = mid + 1
    # 最后需要检查右边界的越界情况，并且不一定存在相等的情况
    if right < 0 or nums[right] != target:
        return -1
    return right


def search_range(nums, target):
    left = left_bound(nums, target)
    right = right_bound(nums, target)
    return [left, right]


print(f'search range for {[5, 7, 7, 8, 8, 10]} is {search_range([5, 7, 7, 8, 8, 10], 8)}')


# https://leetcode-cn.com/problems/search-insert-position/
# 找到合适的位置并插入
def search_for_insert(nums, target):
    left, right = 0, len(nums) - 1

    if not nums:
        return 0

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            # 别返回，锁定左侧边界
            right = mid - 1
    if left >= len(nums):
        return len(nums)
    return left


print(f'search_for_insert for [1, 3, 5, 6] is {search_for_insert([1, 3, 5, 6], 0)}')


# 杨氏矩阵查找
# https://leetcode-cn.com/problems/search-a-2d-matrix/
def search_matrix(matrix, target):
    if not matrix:
        return False

    size_x, size_y = len(matrix), len(matrix[0])
    start_x, start_y = 0, size_y - 1
    while start_x < size_x and start_y >= 0:
        if matrix[start_x][start_y] < target:
            start_x += 1
        elif matrix[start_x][start_y] > target:
            start_y -= 1
        else:
            return True
    return False


# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
# 寻找旋转排序数组中的最小值，没有重复的值
def find_min(nums):
    start, end = 0, len(nums) - 1
    while start < end:
        mid = start + (end - start) // 2
        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            # 因为 nums[mid] <= nums[end] 的情况下是升序，不能确定 end 是升序的第一个值还是升序中间的值，所以 end = mid
            end = mid
    return nums[start]


print(f'find_min for [3, 1, 2] is {find_min([3, 1, 2])}')


# [2,2,2,0,1] ==> 0
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
# 寻找旋转排序数组中的最小值，有重复的值
def find_min_ii(nums):
    start, end = 0, len(nums) - 1
    while start < end:
        mid = start + (end - start) // 2
        if nums[mid] > nums[end]:
            start = mid + 1
        elif nums[mid] < nums[end]:
            # 因为 nums[mid] <= nums[end] 的情况下是升序，不能确定 end 是升序的第一个值还是升序中间的值，所以 end = mid
            end = mid
        else:
            # 当 nums[mid] == nums[end] 的时候不能确定最小元素在 mid 的左边还是右边，最保险的方法是将 end - 1
            end -= 1
    return nums[start]


print(f'find_min for [2, 0, 1, 2, 2] is {find_min_ii([2, 0, 1, 2, 2])}')


# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
# 搜索旋转排序数组
def search_in_rotated_sorted_list(nums, target):
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[0] <= nums[mid]:
            if nums[0] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[len(nums) - 1]:
                l = mid + 1
            else:
                r = mid - 1
    return -1


# https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/
def search_in_rotated_sorted_list_ii(nums, target):
    if not nums:
        return False
    l, r = 0, len(nums) - 1
    start, end = 0, r
    while l <= r:
        if nums[l] == nums[r] and nums[l] != target:
            l += 1
            r -= 1
            start += 1
            end -= 1
            continue
        mid = (l + r) // 2
        if nums[mid] == target:
            return True
        if nums[0] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid
        else:
            if nums[mid] < target <= nums[end]:
                l = mid + 1
            else:
                r = mid
    return False


print(search_in_rotated_sorted_list_ii([1, 3, 1, 1, 1], 3))
