import time
from functools import wraps


# 1
odd_sum = sum([i for i in range(100) if i % 2 == 1])

# 2
duple_list = list()
result = list(set(duple_list))


# 3
def reverse_string(s):
    return s[::-1]


# 4
def timeout(max_time):
    def decorated(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = int(time.time())
            res = func(*args, **kwargs)
            cost = int(time.time()) - start
            print(f"{func.__name__} function ran for {cost} s")
            if cost - start > max_time:
                print(f"{func.__name__} function exceeds max_time")
            return res
        return wrapper
    return decorated


# 5
class InterInt:
    def __init__(self):
        self.a = 1

    def __next__(self):
        temp = self.a
        self.a += 1
        return temp


# 6
class Node(object):
    def __init__(self, key, value, _next=None):
        self.key = key
        self.value = value
        self.next = _next

    def set_next(self, new_node):
        self.next = new_node


class CustomDict:
    def __init__(self):
        self.key_set = set()
        self.key_max_length = 1000
        self.key_list = [None for _ in range(self.key_max_length)]

    def __hash_func(self, key):
        return hash(key) % self.key_max_length

    def __getitem__(self, key):
        if key not in self.key_set:
            raise KeyError(f'{key} not in CustomDict')
        key_index = self.__hash_func(key)
        node = self.key_list[key_index]
        while node:
            if node.key == key:
                return node.value
            node = node.next

    def __setitem__(self, key, value):
        self.key_set.add(key)
        key_index = self.__hash_func(key)
        node = self.key_list[key_index]
        new_node = Node(key, value)
        if not node:
            self.key_list[key_index] = new_node
        else:
            while node:
                node = node.next
            node.set_next(new_node)


# cdict = CustomDict()
# cdict["a"] = 1
# cdict["b"] = 2
# print(cdict["a"])
# print(cdict["c"])

class LinkedNode(object):
    def __init__(self, key, _next=None, pre=None):
        self.key = key
        self.next = _next
        self.pre = pre

    def set_next(self, new_node):
        self.next = new_node

    def set_pre(self, pre):
        self.pre = pre


# 7-1
class Solution:
    def __init__(self):
        # 1 ==> ... ==> 18 ==> 19 ==> 26 ==> ... ==> 30 ==> 25 ==> 31 ==> 32 ==> 33
        #                                                      ^
        #                                                     ||
        #                                                      24
        node_list = [LinkedNode(i) for i in range(1, 34)]
        self.head = node_list[0]
        # 1 ==> ... ==> 18 ==> 19
        for item, next_item in zip(range(0, 32), range(1, 33)):
            node_list[item].set_next(node_list[next_item])
            node_list[next_item].set_pre(node_list[item])

        node_list[25].set_pre(node_list[18])
        node_list[29].set_next(node_list[24])
        node_list[24].set_next(node_list[30])
        node_list[30].set_pre(node_list[24])
        node_list[32].set_next(node_list[0])
        node_list[0].set_pre(node_list[32])

        # # 26 ==> ... ==> 30
        # for item, next_item in zip(range(26, 30), range(27, 31)):
        #     node_list[item].set_next(node_list[next_item])
        #     node_list[next_item].set_pre(node_list[item])
        #
        # # 20 ==> ... ==> 24
        # for item, next_item in zip(range(20, 24), range(21, 25)):
        #     node_list[item].set_next(node_list[next_item])
        #     node_list[next_item].set_pre(node_list[item])
        #
        # # 19 ==> 20
        # node_list[18].set_next(node_list[19])
        # node_list[19].set_pre(node_list[18])
        #
        # # 30 ==> 25
        # node_list[29].set_next(node_list[24])
        # node_list[24].set_pre(node_list[29])
        #
        # # 24 ==> 25
        # node_list[23].set_next(node_list[24])
        # node_list[23].set_pre(node_list[24])
        #
        # # 25 ==> 31 ==> 32 ==> 33
        # node_list[24].set_next(node_list[30])
        # node_list[30].set_pre(node_list[24])
        # node_list[30].set_next(node_list[31])
        # node_list[31].set_pre(node_list[30])
        # node_list[31].set_next(node_list[32])
        # node_list[32].set_pre(node_list[31])

        self.node_list = node_list

    def find_next_node(self, current_position: int, step: int) -> int:
        node = self.node_list[current_position - 1]
        if current_position == 19 and step > 0:
            step -= 1
            node = self.node_list[25]

        if current_position == 25 and step < 0:
            step += 1
            node = self.node_list[29]

        if step > 0:
            while node and step:
                node = node.next
                step -= 1
        else:
            while node and step != 0:
                node = node.pre
                step += 1
        print(node.key)
        return node.key


solution = Solution()
solution.find_next_node(1, 4) # 5
solution.find_next_node(5, -4) # 1
solution.find_next_node(17, 5) # 22
solution.find_next_node(19, 2) # 27
solution.find_next_node(27, -3) # 18
solution.find_next_node(30, 3) # 32
solution.find_next_node(32, -4) # 23
solution.find_next_node(25, -2) # 29
solution.find_next_node(33, 3) # 3
solution.find_next_node(1, -2) # 32


# 7-2
def init_board():
    board = [['.' for _ in range(6)] for _ in range(6)]
    choice_list = [1, 2, 3, 4]

    def helper(i, j):
        # 列，行
        m, n = 5, 5
        if j == n:
            # 下一行
            return helper(i+1, 0)

        if i == m:
            return True

        if board[i][j] != '.':
            return helper(i, j + 1)

        for num in choice_list:
            if not can_insert(i, j, num):
                continue

            board[i][j] = num
            if helper(i, j+1):
                return True

            # 撤销选择
            board[i][j] = '.'

    def can_insert(i, j, num):
        # 少于三个数字
        if i < 4 or j < 4:
            return True

        temp_set = set(set(board[i]))
        temp_set.remove('.')
        temp_set.add(num)
        if len(temp_set) == 3:
            return True

        temp_set1 = set([row[j] for row in board])
        temp_set1.remove('.')
        temp_set1.add(num)
        if len(temp_set1) != 3:
            return True

        return False

    helper(0, 0)
    return board


print(init_board())
