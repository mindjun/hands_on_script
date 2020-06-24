"""
在一个树中找到节点为特定值的路径
"""


class Node(object):
    def __init__(self, val, *args):
        self.val = val
        self.sub_node = list(args)

    def __iter__(self):
        return self.val


r = Node('zufu', *[Node('A', *[Node('a')]), Node('B', *[Node('b'), Node('b1')]), Node('D', *[Node('xiaoming')])])


def find_xiaoming(root, stack, name='xiaoming'):
    if not root:
        return False
    if root.val == name:
        return True

    for node in root.sub_node:
        temp = find_xiaoming(node, stack, name='xiaoming')
        if temp:
            stack.append(node)
            return True
    return False


def find_xiaoming1(_root, _stack, _name='xiaoming'):
    _res = list()

    def helper(root, stack, name='xiaoming'):
        if root.val == name:
            _res.append(stack.copy())
            return

        for node in root.sub_node:
            stack.append(node)
            helper(node, stack, name='xiaoming')
            stack.pop()
    # return False
    helper(_root, _stack, _name)
    print(_res)
    return _res


res = list()
print(find_xiaoming(r, res))
print(res)

res = list()
_res1 = find_xiaoming1(r, res)
print([i.val for i in _res1[0]])


# 观察者模式

# '''
#
#
# 数据结构
# 小明有个庞大的家族
# 定义函数，接受家谱的祖先，输出从祖先到小明这一路上所有的人（为了将家谱简化成一棵树，家谱中只有父亲一支）
# '''
# class Node(object):
#     def __init__(self, val, *args):
#         self.val = val
#         self.sub_node = [Node(i) for i in args]
#
#
# Node('zufu', [Node('A', ['a']), 'B', 'C'])
#
# def find_xiaoming(root, 'xiaoming', stack):
#     if not root:
#         return False
#     if root.val == 'xiaoming':
#         return True
#
#     for node in root.sub_node:
#         temp = find_xiaoming(node, 'xiaoming', stack)
#         if temp:
#             stack.append(temp)
#             return True
#     return False
#
#
# '''
#
# 算法
# 小明要去上补习班，有周六一下午的时间。
# 补习班有很多种选择，起止时间不一。
# 设计算法，让小明能上到尽可能多的补习班。(不考虑课间休息)
# '''
