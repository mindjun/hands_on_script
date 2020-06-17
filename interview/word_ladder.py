import string
from queue import Queue


all_letters = string.ascii_lowercase
start = "hit"
end = "cog"
data_list = ["hot", "dot", "dog", "lot", "log"]


"""
构造字典梯子树
        hit
         |
        hot
         |
    dot     lot
     |       |
    dog     log
"""


class Node(object):
    def __init__(self, data, sub_node=None):
        self.data = data
        sub_node_list = [sub_node] if sub_node else []
        self.sub_node = sub_node_list

    def __repr__(self):
        return '<Node(data={})>'.format(self.data)

    def __str__(self):
        return '<Node(data={})>'.format(self.data)


def build_tree(root):
    temp_data = root.data
    while data_list:
        for i in range(len(temp_data)):
            for char in all_letters:
                new_word = temp_data[:i] + char + temp_data[i+1:]
                if new_word in data_list:
                    new_node = Node(new_word)
                    root.sub_node.append(new_node)
                    data_list.remove(new_word)
        for sub_node in root.sub_node:
            build_tree(sub_node)
    return


def build_tree_1(root):
    temp_data = root.data
    temp_ch_set = set([ch for ch in temp_data])
    # if len(temp_ch_set & set([ch for ch in end])) == len(temp_data) - 1:
    #     new_node = Node(end)
    #     root.sub_node.append(new_node)
    #     return True

    while data_list:
        for word in list(data_list):
            word_ch_set = set([ch for ch in word])
            if len(temp_ch_set & word_ch_set) == len(temp_data) - 1:
                new_node = Node(word)
                root.sub_node.append(new_node)
                data_list.remove(word)
        for sub_node in root.sub_node:
            build_tree(sub_node)
    return


roo = Node(start)
build_tree_1(roo)


def my_print(node):
    if not node.sub_node:
        return

    # print(node.sub_node)
    for temp in node.sub_node:
        print(temp.data)
    for temp in node.sub_node:
        my_print(temp)


my_print(roo)


def my_print_1(node):
    """
    层级遍历
    :param node:
    :return:
    """
    # temp_list = list()
    # temp_list.append(node)
    # while temp_list:
    #     temp_node = temp_list.pop(0)
    #     yield temp_node.data
    #     if len(temp_node.sub_node) > 0:
    #         temp_list.extend(temp_node.sub_node)

    # 使用 queue
    qu = Queue()
    qu.put(node)
    while qu.qsize() != 0:
        temp_node = qu.get(0)
        yield temp_node.data
        if len(temp_node.sub_node) > 0:
            [qu.put(item) for item in temp_node.sub_node]


list1 = my_print_1(roo)
print([item for item in list1])
