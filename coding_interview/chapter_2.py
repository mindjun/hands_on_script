def duplication_in_array(nums):
    """
    3_1
    找出数组中的重复数字
    """
    if not nums:
        return -1

    for index, num in enumerate(nums):
        # index 下标的数字是不是等于 index，排序之后应该是相等的
        if index == num:
            continue
        else:
            # num 和第 num 个数字相等，那么就找到重复的数字了，因为这个数在下标为 index 和 num 都出现过
            if nums[num] == num:
                return num
            # while 循环，将 index 这个数放到下标为 index 的位置
            while nums[index] != index:
                temp_num = nums[index]
                nums[index], nums[temp_num] = nums[temp_num], nums[index]
    return -1


_nums = [2, 3, 1, 0, 2, 5, 3]
print(duplication_in_array(_nums))
print(duplication_in_array(list(range(10))[::-1]))


def find_num_in_matrix(nums, target):
    """
    杨式矩阵查找
    :param nums:
    :param target:
    :return:
    """
    if target > nums[-1][-1] or target < nums[0][0]:
        return False

    x, y = len(nums), len(nums[0])
    start_x, start_y = 0, y - 1
    while start_x < x and start_y >= 0:
        if nums[start_x][start_y] > target:
            start_y -= 1
        elif nums[start_x][start_y] < target:
            start_x += 1
        else:
            return True
    return False


yang_matrix = [[1, 4, 7, 11, 15],
               [2, 5, 8, 12, 19],
               [3, 6, 9, 16, 22],
               [10, 13, 14, 17, 24],
               [20, 21, 23, 26, 30]]
print(find_num_in_matrix(yang_matrix, 31))


# 回溯法，查找路径
def find_path(matrix, target_str):
    """
    查找 matrix 中是否存在 target_str 的路径
    :param matrix:
    :param target_str:
    :return:
    """
    def helper(x, y, index):
        has_path = False
        # 当 index 到达最后一位的时候，直接返回
        if index == len(target_str) - 1 and matrix[x][y] == target_str[index]:
            return True

        if 0 <= x < size_x and 0 <= y < size_y and matrix[x][y] == target_str[index] and not visited[x][y]:
            index += 1
            visited[x][y] = 1
            has_path = helper(x-1, y, index) or helper(x+1, y, index) or helper(x, y-1, index) or helper(x, y+1, index)
            if not has_path:
                index -= 1
                visited[x][y] = 0
        return has_path

    size_x, size_y = len(matrix), len(matrix[0])
    target_index = 0
    visited = [[0 for _ in range(size_y)] for _ in range(size_x)]
    for i in range(size_x):
        for j in range(size_y):
            if helper(i, j, target_index):
                return True
    return False


_matrix = [['a', 'b', 't', 'g'],
           ['c', 'f', 'c', 's'],
           ['j', 'd', 'e', 'h']]
print(find_path(_matrix, 'bfcd'))