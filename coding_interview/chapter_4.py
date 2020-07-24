from typing import List


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


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        if not pushed and not popped:
            return True

        if not pushed:
            return False

        helper_stack = [pushed[0]]
        pushed = pushed[1:]

        while pushed and popped:
            if helper_stack and helper_stack[-1] == popped[0]:
                helper_stack = helper_stack[:-1]
                popped = popped[1:]
            else:
                helper_stack.append(pushed[0])
                pushed = pushed[1:]
        return helper_stack[::-1] == popped


print(Solution().validateStackSequences([1, 0], [1, 0]))


# https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/solution/mian-shi-ti-31-zhan-de-ya-ru-dan-chu-xu-lie-mo-n-2/
def validate_stack_sequences(pushed: List[int], popped: List[int]) -> bool:
    stack, i = [], 0
    for num in pushed:
        stack.append(num)  # num 入栈
        while stack and stack[-1] == popped[i]:  # 循环判断与出栈
            stack.pop()
            i += 1
    return not stack


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode < {self.val} >'


# https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
def level_order(root: TreeNode) -> List[List[int]]:
    node_list = list()

    if not root:
        return node_list

    from collections import deque
    q = deque()
    q.append(root)

    while q:
        tmp = list()
        # 获取当前层的节点数，并处理那么多节点
        now_layer_size = len(q)
        for _ in range(now_layer_size):
            node = q.popleft()
            tmp.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        node_list.append(tmp[::-1] if len(node_list) & 1 else tmp)

    return node_list


t = TreeNode(1, TreeNode(2, left=TreeNode(4)), TreeNode(3, right=TreeNode(5)))
print(level_order(t))
