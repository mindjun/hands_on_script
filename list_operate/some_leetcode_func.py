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
        if nums[left] != nums[right]:
            left += 1
            nums[left], nums[right] = nums[right], nums[left]
    print(f'remove_duplicates num is {nums}')
    return left + 1


print(remove_duplicates([1, 2, 2, 3, 4, 5, 5, 6, 6]))
