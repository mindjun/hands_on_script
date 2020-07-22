# 剑指 offer 28
# https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
def spiral_order(matrix):
    # 从 (0, 0) 开始
    start, result = 0, list()

    if not matrix:
        return result

    rows, columns = len(matrix), len(matrix[0])

    def print_helper():
        max_row, max_col = rows - start, columns - start

        # left ==> right
        for i in range(start, max_col):
            result.append(matrix[start][i])

        # top ==> bottom
        for j in range(start + 1, max_row):
            result.append(matrix[j][max_col - 1])

        # bottom ==> left
        # max_row - 1 != start 再进行添加，避免与 left ==> right 重复
        if max_row - 1 != start:
            for m in range(start, max_col - 1)[::-1]:
                result.append(matrix[max_row - 1][m])

        # bottom ==> top
        # max_col - 1 != start 再进行添加，避免与 top ==> bottom 重复
        if max_col - 1 != start:
            for n in range(start + 1, max_row - 1)[::-1]:
                result.append(matrix[n][start])

    while rows > 2 * start and columns > 2 * start:
        print_helper()
        start += 1

    return result


print(spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
# [1,2,3,4,8,12,11,10,9,5,6,7]


# https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/mian-shi-ti-29-shun-shi-zhen-da-yin-ju-zhen-she-di/
def spiral_order_ii(matrix):
    if not matrix:
        return []
    left, right, top, bottom, result = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, list()

    while True:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        if top > bottom:
            break

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if left > right:
            break

        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

        if top > bottom:
            break

        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

        if left > right:
            break
    return result


print(spiral_order_ii([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
