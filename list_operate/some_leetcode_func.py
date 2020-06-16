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

    zero_index, has_zero = 0, False
    for i in range(len(nums)):
        # 找到第一个不为 0 的下标，如果之前的元素出现了 0，那么交换
        # zero_index 总是小于等于 i
        if nums[i] != 0:
            if has_zero:
                nums[zero_index], nums[i] = nums[i], nums[zero_index]
            zero_index += 1
        else:
            has_zero = True
    return nums


print(move_zero([1, 2, 3, 0, 4, 0, 5, 6, 0, 7, 8]))
# print(move_zero([0, 0, 1]))
