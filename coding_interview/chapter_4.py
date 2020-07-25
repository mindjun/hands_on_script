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


# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
# 后序遍历，根节点一定是最后一个元素，使用该元素将剩下的元素分为左子树和右子树，找到分隔的下标，如果右子树中出现小于根节点值的元素
# 直接返回 False，该序列一定不是后序遍历的序列
def verify_post_order(nums):
    def verify_helper(_nums):
        print(_nums)
        if not _nums:
            return False

        root_num = _nums.pop()

        left_index, left_nums = 0, list()
        for i in range(len(_nums)):
            if _nums[i] > root_num:
                break
            left_index += 1
            left_nums.append(_nums[i])

        for j in range(left_index, len(_nums)):
            if _nums[j] < root_num:
                return False

        left = True
        if left_index > 0:
            left = verify_helper(left_nums)

        right, right_nums = True, _nums[left_index:]
        if left_index < len(_nums) - 1:
            right = verify_helper(right_nums)
        return left and right

    if not nums:
        return True
    return verify_helper(nums)


print(verify_post_order([5, 7, 6, 9, 11, 10, 8]))


# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/
# 使用单调栈进行判断
def verify_post_order_ii(nums):
    stack, root = list(), float('inf')
    # 后序遍历的倒序列表，[根节点|右子树|左子树]
    for num in nums[::-1]:
        if num > root:
            return False
        # 在 stack 找到 num 的父节点
        while stack and stack[-1] > num:
            root = stack.pop()
        stack.append(num)
    return True


# https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/submissions/
# 回溯法进行计算，类似于决策树
class Solution:
    def __init__(self):
        self.sum_func = sum

    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        result = list()

        def back_track(node, path):
            if not node.left and not node.right:
                if self.sum_func(path) == sum_:
                    result.append(path.copy())
                return
            if node.left:
                path.append(node.left.val)
                back_track(node.left, path)
                path.pop()
            if node.right:
                path.append(node.right.val)
                back_track(node.right, path)
                path.pop()
            return

        if not root:
            return []

        back_track(root, [root.val])
        return result


# https://leetcode-cn.com/problems/path-sum-ii/
# dfs 每次带上 path 和当前 sum
def path_sum_ii(root, target):
    result = list()

    def dfs(node, path, _sum):
        if not node:
            return
        if not node.left and not node.right and node.val - _sum == 0:
            result.append(path + [node.val])
            return
        dfs(node.left, path + [node.val], _sum - node.val)
        dfs(node.right, path + [node.val], _sum - node.val)
        return

    dfs(root, [], target)
    return result


_r = TreeNode(5, TreeNode(4, left=TreeNode(11, TreeNode(7), TreeNode(2))),
              TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
print(Solution().pathSum(_r, 22))
print(path_sum_ii(_r, 22))


# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/solution/mian-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/
def bst_to_double_linked(root):
    if not root:
        return None
    _head, pre = None, None

    def dfs(cur):
        if not cur:
            return
        dfs(cur.left)
        nonlocal pre
        nonlocal _head
        if pre:
            pre.right, cur.left = cur, pre
        else:
            _head = cur
        # 不断替换 pre 为 cur，中序遍历，第一次 return 的时候，pre 为 None， cur 为最左边的叶节点
        # 此时将 pre 设置为 cur，即最左边的叶节点，下一个即将访问的节点就是该节点的父节点
        pre = cur
        dfs(cur.right)

    dfs(root)
    _head.left, pre.right = pre, _head
    return _head


# https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/hui-su-fa-by-ai-wu-jin-xin-fei-xiang/
class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s:
            return []
        s = list(sorted(s))
        res = []

        def helper(_s, tmp):
            if not _s:
                res.append(''.join(tmp))
            for i, char in enumerate(_s):
                if i > 0 and _s[i] == _s[i - 1]:
                    continue
                helper(_s[:i] + _s[i + 1:], tmp + [char])

        helper(s, [])
        return res


# # 使用回溯的时候会遇到一些重复字符的错误
# # 需要先进行排序 ？
# def permutation(s):
#     if not s:
#         return []
#
#     result_list = list()
#
#     def back_pack(s_, track):
#         if not s_:
#             result_list.append(''.join(track))
#             return
#
#         for idx, ch in enumerate(s_):
#             # 有可能回出现重复的字符，如果当前的字符已经处理过，就跳过
#             if idx > 0 and s_[idx] == s_[idx - 1]:
#                 continue
#             track.append(ch)
#             back_pack(s_[:idx] + s_[idx + 1:], track)
#             track.pop()
#
#     # 先进行排序
#     s = list(sorted(s))
#     back_pack(s, [])
#     return result_list
#
#
# print(permutation('aab'))
