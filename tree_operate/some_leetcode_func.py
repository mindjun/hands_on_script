

# N 叉树的前序遍历
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
def pre_order(root):
    stack, res = [root], list()
    while stack:
        node = stack.pop()
        if not node:
            continue

        res.append(node.val)
        while node.children:
            # 因为是前序遍历，所以下一次处理的是该节点的第一个自节点，于是将所有孩子倒序后添加到 stack 中
            stack.extend(node.children[::-1])
            node = stack.pop()
            res.append(node.val)
    return res


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


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
def min_depth(root: TreeNode) -> int:
    if not root:
        return 0

    children = [root.left, root.right]
    if not any(children):
        return 1

    depth = float('inf')
    for c in children:
        if c:
            depth = min(min_depth(c), depth)
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
