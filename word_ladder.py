# coding=utf-8

import string

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


roo = Node(start)
build_tree(roo)


def my_print(node):
    if not node.sub_node:
        return

    print(node.sub_node)
    for temp in node.sub_node:
        print(temp.data)
    for temp in node.sub_node:
        my_print(temp)


my_print(roo)

