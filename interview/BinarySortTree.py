# 二叉树遍历框架
# void traverse(TreeNode root) {
#     // root 需要做什么？在这做。
#     // 其他的不用 root 操心，抛给框架
#     traverse(root.left);
#     traverse(root.right);
# }
from queue import Queue

from collections import defaultdict


class BSTNode(object):
    # 二叉树的节点
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySortTree(object):
    # 基于二叉树节点的二叉排序树
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def clear(self):
        # 清除该树
        self._root = None

    def get_root(self):
        return self._root

    def insert_1(self, value, rt=None):
        """
        递归方法实现
        :param value:
        :param rt:
        :return:
        """
        if self.is_empty():
            self._root = BSTNode(value)
            return self._root
        rt = rt if rt else self._root
        # 如果已经存在，直接返回
        if rt.data == value:
            return rt
        if value > rt.data:
            rt.right = self.insert_1(value, rt.right)
        if value < rt.data:
            rt.left = self.insert_1(value, rt.left)
        return rt

    def insert(self, value):
        if self.is_empty():
            self._root = BSTNode(value)
            return
        rt = self._root
        while True:
            if value > rt.data:
                if rt.right is None:    
                    rt.right = BSTNode(value)
                    return
                rt = rt.right
            elif value < rt.data:
                if rt.left is None:
                    rt.left = BSTNode(value)
                    return
                rt = rt.left
            else:
                print('data existed !')
                return

    def search(self, value):
        # 查找，返回查询节点或者None
        rt = self._root
        while True:
            if rt.data == value:
                return rt
            elif rt.data > value:
                rt = rt.left
            else:
                rt = rt.right
            if rt is None:
                return None

    def reverse_tree_node1(self, rt):
        """
        交换二叉树左右节点，递归实现
        :param rt:
        :return:
        """
        if not rt:
            return
        rt.left, rt.right = rt.right, rt.left
        self.reverse_tree_node1(rt=rt.left)
        self.reverse_tree_node1(rt=rt.right)

    def invert_tree(self, rt=None):
        """
        交换二叉树的左右节点
        :param rt:
        :return:
        """
        if not rt:
            rt = self._root
        rt.left, rt.right = rt.right, rt.left
        if rt.left:
            self.invert_tree(rt.left)
        if rt.right:
            self.invert_tree(rt.right)
        return rt

    def reverse_tree_node(self, rt=None):
        """
        交换二叉树的左右节点
        :param rt:
        :return:
        """
        if not rt:
            rt = self._root
        stack = list()
        stack.append(rt)
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    def __iter__(self, rt=None):
        # 遍历的非递归实现
        # 遍历中使用列表作为栈，来保存先后走过的路径
        if rt is None:
            rt = self._root
        stack = []
        # 中序遍历
        # 将rt入栈，若rt的左孩子不为空，将其入栈，并将rt的左孩子设为当前rt
        #          若左孩子为空，取出栈顶元素，访问，然后将栈顶元素的右孩子设为当前节点
        while stack or rt:
            while rt:
                stack.append(rt)
                rt = rt.left
            rt = stack.pop()
            yield rt
            # 存在节点没有左孩子但是有右孩子的情况
            rt = rt.right

    def pre_travel(self, rt=None):
        # 前序遍历
        # 访问rt，并将rt入栈
        # 判断rt的左子树或者rt是否为空，若为空取栈顶元素，并将栈顶元素的右孩子设为rt
        #                            若不为空，将rt的左孩子设为rt
        # 直到 stack为空或者rt为空，结束遍历
        # if rt is None:
        #     rt = self._root
        # stack = list()
        # while stack or rt:
        #     if rt is not None:
        #         yield rt
        #         stack.append(rt)
        #     if rt is None or rt.left is None:
        #         rt = stack.pop()
        #         rt = rt.right
        #     else:
        #         rt = rt.left

        if rt is None:
            rt = self._root
        stack = list()
        while rt or stack:
            while rt:
                yield rt
                stack.append(rt)
                rt = rt.left
            rt = stack.pop()
            rt = rt.right

    def post_travel(self, rt=None):
        # 后序遍历
        if rt is None:
            rt = self._root

        # 将根节点入栈，设置pre为前一次访问的节点
        # 只有当栈顶元素没有左右孩子或者他的左右孩子已经被访问的情况下才能访问该节点
        # 否则依次将改节点的右孩子、左孩子入栈
        # stack = list()
        # stack.append(rt)
        # pre = None
        # while stack:
        #     rt = stack[-1]
        #     if (rt.left is None and rt.right is None) or (pre is not None and (pre is rt.left or pre is rt.right)):
        #         yield rt
        #         pre = stack.pop()
        #     else:
        #         if rt.right:
        #             stack.append(rt.right)
        #         if rt.left:
        #             stack.append(rt.left)

        stack = list()
        # 通过 last_visit 来判断右节点是否已经弹出
        last_visit = None
        while stack or rt:
            while rt:
                stack.append(rt)
                rt = rt.left
            # 这里不弹出，先取出来看看
            node = stack[-1]
            # 保证根节点在右节点之后弹出
            if not node.right or node.right == last_visit:
                stack.pop()
                yield node
                last_visit = node
            else:
                rt = node.right

    def layer_travel(self, rt=None):
        # 层级遍历
        # 使用队列，先进先出
        # 将根节点推入队列，访问根节点，分别判断根节点的左右节点，并将其推入队列
        # 每次从队列中取出一个元素并访问，并判断其左右子节点是否为空，将子节点推入队列
        # 循环的退出条件为队列为空
        # from my_queue import Queue
        if rt is None:
            rt = self._root
        qu = Queue()
        qu.put(rt)
        while not qu.empty():
        # while qu.qsize() != 0:
            node = qu.get_nowait()
            yield node
            if node.left:
                qu.put(node.left)
            if node.right:
                qu.put(node.right)

    def layer_travel_with_depth(self, rt=None):
        travel_road = defaultdict(list)
        if rt is None:
            rt = self._root
        queue = Queue()
        dep = 0
        queue.put((rt, dep))
        while not queue.empty():
            node, depth = queue.get_nowait()
            travel_road[depth].append(node.data)
            if node.left:
                queue.put((node.left, depth + 1))
            if node.right:
                queue.put((node.right, depth + 1))
        return travel_road

    def layer_travel_1(self, rt=None):
        """
        按照每一层，从左到右进行打印
        :param rt:
        :return:
        """
        res = defaultdict(list)
        if rt is None:
            rt = self._root

        def helper(root, deep):
            if not root:
                return

            res[deep].append(root.data)
            helper(root.left, deep + 1)
            helper(root.right, deep + 1)

        helper(rt, 0)
        return res

    def delete(self, value, root=None):
        # 先找到该节点，再删除
        if root is None:
            return root
        if root.data == value:
            # do delete
            # 左子数为空，返回右子树
            if root.left is None:
                return root.right
            # 右子数为空，返回左子树
            if root.right is None:
                return root.left
            # 左右子树都不为空，找到右子树的最小节点，并删除
            min_node = self._get_min_node(root.right)
            # 交换 root 与 min_node 的 data 值，然后删除 min_node 的 data 值
            # 复杂点的操作，会交换 root 节点与 min_node 节点（修改指针的指向来完成），然后删除 root 来完成
            root.data = min_node.data
            root.right = self.delete(min_node.data, root.right)
        elif root.data > value:
            root.left = self.delete(value, root.left)
        elif root.data < value:
            root.right = self.delete(value, root.right)
        return root

    @staticmethod
    def _get_min_node(node):
        while node.left:
            node = node.left
        return node

    # 递归实现遍历
    def pre_order(self, node):
        if node is None:
            return
        pre_order_list.append(node.data)
        # print(node.data)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        in_order_list.append(node.data)
        self.in_order(node.right)
    
    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        post_order_list.append(node.data)

    def is_valid_bst(self, root=None):
        if not root:
            root = self._root
        return self.is_valid_bst_help(root, None, None)

    def is_valid_bst_help(self, root, min_node, max_node):
        if root is None:
            return True
        if min_node and root.data < min_node.data:
            return False
        if max_node and root.data > max_node.data:
            return False
        return self.is_valid_bst_help(root.left, min_node, root) and self.is_valid_bst_help(root.right, root, max_node)

    def node_count(self, rt):
        """
        统计节点数量
        :param rt:
        :return:
        """
        # 如果是完全二叉树，可以利用二叉树的特点，计算出高度，然后 2^h - 1 就是树节点数
        # left, right = rt or rt.left, rt or rt.right
        # hl, hr = 0, 0
        # while left:
        #     left = left.left or left.right
        #     hl += 1
        # while right:
        #     right = right.right or right.left
        #     hr += 1
        # if hl == hr:
        #     return pow(2, hl) - 1
        # return 1 + self.node_count(rt.left) + self.node_count(rt.right)

        if not rt:
            return 0
        return 1 + self.node_count(rt.left) + self.node_count(rt.right)

    @staticmethod
    def tree_high(root):
        left_high, right_high = 0, 0
        left, right = root, root
        while left:
            left = left.left
            left_high += 1
        while right:
            right = right.right
            right_high += 1
        return left_high, right_high


if __name__ == '__main__':
    list1 = [46, 29, 12, 32, 59, 98, 57, 92]
    bin_sort = BinarySortTree()
    for item in list1:
        bin_sort.insert(item)

    print([i.data for i in bin_sort])
    print(f'节点数为 : {bin_sort.node_count(bin_sort.get_root())}')
    print(f'层序遍历: {bin_sort.layer_travel_1()}')
    print(f'队列层序遍历: {bin_sort.layer_travel_with_depth()}')
    # bin_sort.reverse_tree_node1(bin_sort._root)
    # print([i.data for i in bin_sort])
    # bin_sort.reverse_tree_node()
    # print([i.data for i in bin_sort])

    print(f'是否是合法的 BST: {bin_sort.is_valid_bst()}')
    # node_map = list((map(bin_sort.insert, list1)))
    item_list = [item.data for item in bin_sort]
    print('非递归前序遍历： {}'.format([item.data for item in bin_sort.pre_travel()]))
    print('非递归中序遍历： {}'.format(item_list))
    print('非递归后序遍历： {}'.format([item.data for item in bin_sort.post_travel()]))

    print('非递归层级遍历： {}'.format([item.data for item in bin_sort.layer_travel()]))

    # 递归遍历操作
    pre_order_list = list()
    bin_sort.pre_order(bin_sort.get_root())
    print('递归前序遍历: {}'.format(pre_order_list))
    in_order_list = list()
    bin_sort.in_order(bin_sort.get_root())
    print('递归中序遍历: {}'.format(in_order_list))
    post_order_list = list()
    bin_sort.post_order(bin_sort.get_root())
    print('递归后序遍历: {}'.format(post_order_list))

    delete_value = bin_sort.delete(92)
    print('删除元素: {}'.format(delete_value))

    item_list1 = [item.data for item in bin_sort]
    print('删除元素：{}'.format(item_list1))

    # revert = bin_sort.invert_tree()
    # print(f'翻转后为 : {[item.data for item in revert]}')
