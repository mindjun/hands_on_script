"""
杨式矩阵查找
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
"""
import math

yang_matrix = [[1, 4, 7, 11, 15],
               [2, 5, 8, 12, 19],
               [3, 6, 9, 16, 22],
               [10, 13, 14, 17, 24],
               [20, 21, 23, 26, 30]]


# 主要思想来源于二分法，但是因为左上角往右和往下都是递增，比较数字后无法判断是往哪个方向进行
# # 所以需要判断，大于和小于分别走哪个方向进行，可以把起点设置为右上或者左下

def solution1(matrix, target):
    max_y = len(matrix[0]) - 1
    max_x = len(matrix) - 1
    if target < matrix[0][0] or target > matrix[max_x][max_y]:
        return False
    # 从右上角开始
    start_y = 0
    start_x = len(matrix) - 1
    while start_x >= 0 and start_y <= max_y:
        if target > yang_matrix[start_y][start_x]:
            start_y += 1
        elif target < yang_matrix[start_y][start_x]:
            start_x -= 1
        else:
            return True, start_x, start_y
    return False, start_x, start_y


print(solution1(yang_matrix, 20))


# 二分算法
# 从矩阵中间行或者中间列或者对角线开始查找，找到s满足 ai < s < ai+1 ,  其中ai为矩阵中的值。
# 通过行、列或者对角线将矩阵分为两个更小的矩阵

def solution2(sub_matrix, num, target):
    """
    按照行处理
    :param sub_matrix: 需要处理的子矩阵
    :param num: 行数最大值，以便进行二分
    :param target: 目标值
    :return:
    """
    if num == 0:
        return False
    mid = math.floor(num / 2)
    # print(mid)
    # 这里可以使用二分查找
    if target in sub_matrix[mid]:
        return True
    lie = len([item for item in sub_matrix[mid] if item < target])
    # print(lie)
    part_1 = [line[:lie] for line in sub_matrix[mid + 1:]]
    part_2 = [line[lie:] for line in sub_matrix[:mid]]
    # print(part_1)
    # print(part_2)
    return solution2(part_1, len(part_1), target) or solution2(part_2, len(part_2), target)


# for item in [1, 4, 7, 11, 15,2, 5, 8, 12, 19,3, 6, 9, 16, 22,10,13,14,17, 24,20,21,23,26,30]:
#     print(solution2(yang_matrix, len(yang_matrix), item))

print(solution2(yang_matrix, len(yang_matrix), 18))
