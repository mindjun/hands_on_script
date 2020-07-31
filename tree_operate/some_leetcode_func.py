# void traverse(TreeNode root) {
#     // root 需要做什么？在这做。
#     // 其他的不用 root 操心，抛给框架
#     traverse(root.left);
#     traverse(root.right);
# }
from typing import List


# N 叉树的前序遍历
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
def pre_order(root):
    stack, res = [root], list()
    # while stack:
    #     node = stack.pop()
    #     if not node:
    #         continue
    #
    #     res.append(node.val)
    #     while node.children:
    #         # 因为是前序遍历，所以下一次处理的是该节点的第一个自节点，于是将所有孩子倒序后添加到 stack 中
    #         stack.extend(node.children[::-1])
    #         node = stack.pop()
    #         res.append(node.val)
    # return res

    # 递归
    def helper(node):
        if not node:
            return
        res.append(node.val)
        for child in node.children:
            helper(child)
    helper(root)
    return res


# N 叉树的后序遍历
# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
def post_order(root):
    res = list()

    # 递归
    # def helper(node):
    #     if not node:
    #         return
    #     for child in node.children:
    #         helper(child)
    #     res.append(node.val)
    # helper(root)
    # return res

    # 迭代
    if not root:
        return res
    stack = [root]
    while stack:
        node = stack.pop()
        # 根 右 左 的顺序入栈
        res.append(node.val)
        stack.extend(node.children)
    # 将结果倒序即可
    return res[::-1]


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode < {self.val} >'


# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
# 二叉树的序列化与反序列化
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(node):
            if node:
                node_list.append(node.val)
                dfs(node.left)
                dfs(node.right)
            else:
                node_list.append("#")

        node_list = []
        dfs(root)
        return ",".join([str(i) for i in node_list])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def dfs():
            v = next(node_list)
            if v == "#":
                return None
            node = TreeNode(int(v))
            node.left = dfs()
            node.right = dfs()
            return node

        node_list = iter(data.split(","))
        return dfs()


class SelfCodec(object):
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        # 前序遍历
        # 考虑将二叉树补全为一棵满二叉树进行操作，遇到没有的节点就设置为 None
        res = list()
        temp = list()
        stack = [(root, 0)]
        while stack:
            node, index = stack.pop()
            if node:
                temp.append((node.val, index))
                stack.append((node.left, 2 * index + 1))
                stack.append((node.right, 2 * index + 2))
        temp.sort(key=lambda x: x[-1])
        all_index = set([i[-1] for i in temp])
        node_count = temp[-1][-1] + 1
        res_index = 0
        for i in range(node_count):
            if i in all_index:
                res.append(str(temp[res_index][0]))
                res_index += 1
            else:
                res.append('None')
        return ','.join(res)

        # res, node_list = list(), list()
        #
        # def helper(_root, _index):
        #     if not _root:
        #         return
        #     node_list.append((_root.val, _index))
        #     helper(_root.left, 2 * _index + 1)
        #     helper(_root.right, 2 * _index + 2)
        #
        # helper(root, 0)
        # node_count = node_list[-1][-1] + 1
        # all_index = set([i[-1] for i in node_list])
        # res_index = 0
        # for i in range(node_count):
        #     if i in all_index:
        #         res.append(str(node_list[res_index][0]))
        #         res_index += 1
        #     else:
        #         res.append('None')
        #
        # return ','.join(res)

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        value_list = data.split(',')

        def helper(index):
            if index > len(value_list):
                return None
            if value_list[index] == 'None':
                return None
            root = TreeNode(int(value_list[index]))
            root.left = helper(2 * index + 1)
            root.right = helper(2 * index + 2)
            return root

        return helper(0)


_root = TreeNode(1)
_root.left = TreeNode(2)
_right = TreeNode(3)
_right.left = TreeNode(6)
_right.right = TreeNode(7)
_root.right = _right

print(Codec().serialize(_root))
_res = SelfCodec().deserialize('1,2,3,None,None,6,7')
print(_res)


# 二叉树的最大深度，使用 bfs 求解
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
def max_depth(root: TreeNode) -> int:
    if root:
        level = [root]  # 当前层所有 node
        depth = 0
        while level:
            new_level = []
            for node in level:
                if node:
                    new_level.extend([node.left, node.right])
            level = new_level
            # 当 level 不为空的时候才增加 depth
            if level:
                depth += 1
        return depth
    return 0

    # 递归解法
    # return 0 if not root else max(max_depth(root.left), max_depth(root.right)) + 1


# 二叉树的最小深度，使用 dfs 求解
def _min_depth(root: TreeNode) -> int:
    if not root:
        return 0

    children = [root.left, root.right]
    if not any(children):
        return 1

    depth = float('inf')
    for c in children:
        if c:
            depth = min(_min_depth(c), depth)
    return depth + 1


# 递归求解
def min_depth(root):
    if not root:
        return 0
    left_depth = min_depth(root.left)
    right_depth = min_depth(root.right)
    # 如果左子树深度、右子树深度均不为0，则用min取其中最小值
    # 如果有一个为0，取其中非0的数；都为0，取0
    depth = min(left_depth, right_depth) if left_depth and right_depth else left_depth or right_depth
    return depth + 1


# 二叉树的最小深度，使用 bfs 求解
# 因为 dfs 需要遍历每一个节点，才能保证找到深度最小的节点
# 使用 bfs 只需要找到第一个访问到的叶子节点即可返回
def min_depth_bfs(root: TreeNode) -> int:
    if not root:
        return 0

    from queue import Queue
    queue = Queue()
    queue.put((1, root))
    while queue.qsize():
        depth, node = queue.get_nowait()
        children = [node.left, node.right]
        # 找到了叶子节点
        if not any(children):
            return depth
        for c in children:
            queue.put((depth + 1, c))


# https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/solution/shou-hui-tu-jie-fei-di-gui-fa-zhong-gou-chu-er-cha/
def build_tree(_tree_str):
    def helper(tree_str, deep=0):
        if not tree_str:
            return None
        while tree_str[0] == '_':
            tree_str = tree_str[1:]
        node_value = ''

        while len(tree_str) and tree_str[0].isalnum():
            node_value = node_value + tree_str[0]
            tree_str = tree_str[1:]

        root = TreeNode(node_value)

        # todo 关键在于找到下一层的标识，即有几个 '-'，以层级的标识拆分字符串，然后递归构建左右子树
        # split_flag = '_' * (deep + 1)
        # split_index = 0
        # for i in range(len(tree_str) - len(split_flag)):
        #     a = tree_str[i:i+len(split_flag)]
        #     b = tree_str[i+len(split_flag)].isalnum()
        #     c = i+len(split_flag)
        #     if i != 0 and tree_str[i:i+len(split_flag)] == split_flag and tree_str[i+len(split_flag)].isalnum():
        #         split_index = i
        #         break
        # 以下 split_index 仅针对 1-2--3--4-5--6--7
        split_index = 0
        if deep == 0:
            split_index = 8
        if deep == 1:
            split_index = 3

        root.left = helper(tree_str[:split_index], deep + 1)
        root.right = helper(tree_str[split_index:], deep + 1)
        return root

    __root = helper(_tree_str)
    return __root


# https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/solution/shou-hui-tu-jie-fei-di-gui-fa-zhong-gou-chu-er-cha/
def convert_pre_order(s):
    # 使用栈来保存当前处理的节点
    stack = list()
    i = 0

    while i < len(s):
        cur_level = 0
        # 获取当前的层数
        while i < len(s) and s[i] == '-':
            cur_level += 1
            i += 1

        # 获取当前的节点值
        cur_value = 0
        while i < len(s) and s[i].isalnum():
            cur_value = cur_value * 10 + int(s[i])
            i += 1

        node = TreeNode(cur_value)

        # stack 为空时，node 为根节点
        if not stack:
            stack.append(node)
            continue

        # 当 stack 长度大于 cur_level 时说明当前节点的父节点不是 stack[-1]，删除最后一个节点，直到找到该节点的父节点
        while len(stack) > cur_level:
            stack.pop()

        if not stack[-1].left:
            stack[-1].left = node
        else:
            stack[-1].right = node

        # 将当前节点添加到 stack 中
        stack.append(node)

    # 根节点一定是第一个节点
    return stack[0]


print(convert_pre_order('1-2--3--4-5--6--7'))


# https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/
def build_tree_from_pre_in_order(pre_nums, in_nums):
    """
    根据前序遍历和中序遍历结果，重建二叉树
    每次递归，取出前序遍历的第一个节点，使用该节点将中序数组分为左子树的中序数组和右子树的中序数组，然后再分别根据左右中序数组得到左右前序数组，进入下一次递归
    :param pre_nums:
    :param in_nums:
    :return:
    """
    if not pre_nums or not in_nums:
        return None
    root = TreeNode(pre_nums[0])
    in_index = in_nums.index(pre_nums[0])

    # 新的中序节点
    left_part = in_nums[:in_index]
    right_part = in_nums[in_index+1:]

    # 新的前序节点
    left_pre = [i for i in pre_nums if i in left_part]
    right_pre = [i for i in pre_nums if i in right_part]

    root.left = build_tree_from_pre_in_order(left_pre, left_part)
    root.right = build_tree_from_pre_in_order(right_pre, right_part)
    return root


_pre_nums = [1, 2, 4, 7, 3, 5, 6, 8]
_in_nums = [4, 7, 2, 1, 5, 3, 8, 6]
_root = build_tree_from_pre_in_order(_pre_nums, _in_nums)
print(_root)


# https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/solution/mian-shi-ti-07-zhong-jian-er-cha-shu-di-gui-fa-qin/
# 前序遍历特点： 节点按照 [ 根节点 | 左子树 | 右子树 ] 排序，以题目示例为例：[ 3 | 9 | 20 15 7 ]
# 中序遍历特点： 节点按照 [ 左子树 | 根节点 | 右子树 ] 排序，以题目示例为例：[ 9 | 3 | 15 20 7 ]
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.dic, self.po = {}, preorder
        # 将 inorder 的值与下标 hash，以便能根据 preorder 的值快速获得 inorder 的下标，并区分左子树和右子树
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.recur(0, 0, len(inorder) - 1)

    def recur(self, pre_root, in_left, in_right):
        if in_left > in_right:
            return None  # 终止条件：中序遍历为空
        root = TreeNode(self.po[pre_root])  # 建立当前子树的根节点
        i = self.dic[self.po[pre_root]]    # 搜索根节点在中序遍历中的索引，从而可对根节点、左子树、右子树完成划分。
        # 开启左子树的下层递归，下一个 pre_order 就是 pre_root+1,
        # 中序子树依然遵循 [ 左子树 | 根节点 | 右子树 ] 的规则
        root.left = self.recur(pre_root + 1, in_left, i - 1)
        # 右子树的 pre_root 下标为 根节点索引 + 左子树长度 + 1
        root.right = self.recur(i - in_left + pre_root + 1, i + 1, in_right) # 开启右子树的下层递归
        return root  # 返回根节点，作为上层递归的左（右）子节点


# https://leetcode-cn.com/problems/symmetric-tree/
def is_symmetric(root):
    """
    判断二叉树是否镜像对称
    :param root:
    :return:
    """
    if not root:
        return True

    __root = root
    stack, node_list = list(), list()
    # 中序遍历
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        node_list.append(root)
        root = root.right

    # 根据 __root 将 node_list 分为左右两个列表，如果是镜像对称，那么左右列表倒序应该是相等的
    root_index = 0
    for i in range(len(node_list)):
        if node_list[i] == __root:
            root_index = i
            break
    if root_index == 0 or root_index > len(node_list) // 2:
        return False
    left, right = node_list[:root_index], node_list[root_index + 1:]
    return [n.val for n in left] == [n.val for n in right][::-1]


# 递归实现
def is_symmetric_(root):
    def helper(left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        return left.val == right.val and helper(left.right, right.left) and helper(left.left, right.right)

    return helper(root, root)


_root = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                 right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)))
is_symmetric(_root)


# https://leetcode-cn.com/problems/flip-equivalent-binary-trees/
# 翻转等价二叉树
def flip_equiv(root1, root2):
    if root1 is root2:
        return True
    if not root1 or not root2 or root1.val != root2.val:
        return False

    return (flip_equiv(root1.left, root2.left) and flip_equiv(root1.right, root2.right) or
            flip_equiv(root1.left, root2.right) and flip_equiv(root1.right, root2.left))


# https://leetcode-cn.com/problems/flip-equivalent-binary-trees/solution/shen-du-you-xian-bian-li-by-15011272359-2/
# dfs 深度优先遍历每一个节点
def dfs_flip_equiv(root_1: TreeNode, root_2: TreeNode) -> bool:
    def dfs(root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        if dfs(root1.left, root2.right) and dfs(root1.right, root2.left):
            return True
        if dfs(root1.left, root2.left) and dfs(root1.right, root2.right):
            return True
        return False

    return dfs(root_1, root_2)


# 所有可能的满二叉树
def all_possible_fbt(n):
    res = list()
    root = TreeNode(0)

    # 要么有两个孩子，要么一个都没有
    def helper(_root, node, count):
        if count == n - 1:
            res.append(_root)


# https://leetcode-cn.com/problems/all-possible-full-binary-trees/
class Solution:
    # 子问题：构造一棵满二叉树
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        res = []
        if N == 1:
            return [TreeNode(0)]
        # 结点个数必须是奇数
        if N % 2 == 0:
            return []

        # 左子树分配一个节点
        left_num = 1
        # 右子树可以分配到 N - 1 - 1 = N - 2 个节点
        right_num = N - 2

        while right_num > 0:
            # 递归构造左子树
            left_tree = self.allPossibleFBT(left_num)
            # 递归构造右子树
            right_tree = self.allPossibleFBT(right_num)
            # 具体构造过程
            for i in range(len(left_tree)):
                for j in range(len(right_tree)):
                    root = TreeNode(0)
                    root.left = left_tree[i]
                    root.right = right_tree[j]
                    res.append(root)
            left_num += 2
            right_num -= 2

        return res


# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# https://zhuanlan.zhihu.com/p/152200298?utm_source=wechat_session&utm_medium=social&utm_oi=582127545428873216
def path_sum(root, sum_):
    result = list()

    def dfs(node, path):
        # 因为是要到叶子节点的总和，所以结束条件为 node 的左右孩子都为空
        if not node.left and not node.right:
            # 如果 path 的值加上当前节点的值满足条件，说明找到一个答案
            if sum(path + [node.val]) == sum_:
                result.append(list(path + [node.val]))
        if node.left:
            # 每次递归时带上当前的 path
            dfs(node.left, path + [node.val])
        if node.right:
            dfs(node.right, path + [node.val])

    dfs(root, [])
    return result


# def path_sum_ii(root, target):
#     result = list()
#
#     def dfs(node, path, _sum):
#         if not node:
#             return
#         if not node.left and not node.right and node.val - _sum == 0:
#             result.append(path + [node.val])
#             return
#         dfs(node.left, path + [node.val], _sum - node.val)
#         dfs(node.right, path + [node.val], _sum - node.val)
#         return
#
#     dfs(root, [], target)
#     return result


_root = TreeNode(10, left=TreeNode(6, left=TreeNode(5, right=TreeNode(9)), right=TreeNode(2)),
                 right=TreeNode(7, left=TreeNode(1), right=TreeNode(8)))
_res = path_sum(_root, 18)
print(_res)


# https://leetcode-cn.com/problems/path-sum-iii/
# 路径总和
def path_sum_count(root, sum_):
    def dfs(node, path):
        if not node:
            return 0
        path = [p + node.val for p in path]
        # 因为当前 node 的值可能就等于 sum_，所以先加入到 path 中
        path.append(node.val)

        result = 0
        result += len([i for i in path if i == sum_])

        return result + dfs(node.left, path) + dfs(node.right, path)

    return dfs(root, [])


# https://leetcode-cn.com/problems/check-balance-lcci/
# 判断树是否是平衡
def is_balance_tree(root):
    # 双层递归
    # def get_max_depth(node):
    #     return 0 if not node else max(get_max_depth(node.left), get_max_depth(node.right)) + 1
    # if not root:
    #     return True
    # 判断当前 root 节点是否是平衡
    # if abs(get_max_depth(root.left) - get_max_depth(root.right)) > 1:
    #     return False
    # 递归判断 root 的左右子节点是否平衡
    # return is_balance_tree(root.left) and is_balance_tree(root.right)

    # 使用全局 flag 来标示
    flag = True

    def is_balance_helper(node):
        nonlocal flag

        if not node:
            return 0

        # 计算树深度的同时判断是否是平衡树
        left_depth = is_balance_helper(node.left) + 1
        right_depth = is_balance_helper(node.right) + 1

        if abs(left_depth - right_depth) > 1:
            flag = False

        return max(left_depth, right_depth)

    is_balance_helper(root)
    return flag


# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
# 给定一个非空二叉树，返回其最大路径和。
class MaxPathSum(object):
    def __init__(self):
        self.max_sum = float('-inf')

    def get_max_path_sum(self, root):
        def helper(node):
            if not node:
                return 0
            # 左子树的和
            left = max(helper(node.left), 0)
            # 右子树的和
            right = max(helper(node.right), 0)
            # 当前节点的和
            max_now = node.val + left + right
            # 更新最大值
            self.max_sum = max(self.max_sum, max_now)
            return node.val + max(left, right)

        helper(root)
        return self.max_sum

    def get_max_path_sum_1(self, root):
        # todo 节点的值可能小于 0, 所以不能直接返回 0
        # 左子树最大路径和最大，右子树最大路径和最大，左右子树最大加根节点最大
        if not root:
            return 0
        left = self.get_max_path_sum_1(root.left)
        right = self.get_max_path_sum_1(root.right)
        return max(left, right, left+right+root.val)


# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
# 分治法，有左子树的公共祖先或者有右子树的公共祖先，就返回子树的祖先，否则返回根节点
def lowest_common_ancestor(root, p, q):
    if not root:
        return root
    if root.val == p.val or root.val == q.val:
        return root

    # 递归一定是从最底部开始返回的，所以最先返回的一定是 p q 的最近父节点
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left or right or None


def layer_travel(root):
    from collections import defaultdict
    result = defaultdict(list)

    def helper(node, deep):
        if not node:
            return
        result[deep].append(node.val)
        helper(node.left, deep + 1)
        helper(node.right, deep + 1)

    helper(root, 0)
    print(result)
    for i in result.keys():
        if i % 2 == 1:
            result[i] = result[i][::-1]
    return list(result.values())
    # print(result)


print(layer_travel(_root))


# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
def generate_tree(n):
    def generate_tree_rec(i, j):
        if i > j:
            return [None]

        result = list()
        for m in range(i, j+1):
            left = generate_tree_rec(i, m-1)
            right = generate_tree_rec(m+1, j)

            for l in left:
                for r in right:
                    result.append(TreeNode(m, l, r))
        return result

    return generate_tree_rec(1, n) if n > 0 else []
