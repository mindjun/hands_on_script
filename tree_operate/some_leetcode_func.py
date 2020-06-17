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
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
right = TreeNode(3)
right.left = TreeNode(6)
right.right = TreeNode(7)
_root.right = right

print(Codec().serialize(_root))
_res = Codec().deserialize('1,2,3,None,None,6,7')
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
            depth += 1
        # 当最底层节点加入到 new_level 之后 depth 加了 1，但是这已经是最底层了，下一次循环的时候 level 是空
        # 所以最后的结果返回的时候需要 -1
        return depth - 1
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
