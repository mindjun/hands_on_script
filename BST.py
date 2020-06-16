#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-16 16:47:55

class Node(object):
    """docstring for Node"""
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def getNode(self):
        return self.data

    def setNode(self, newData):
        self.data = newData
        return self.data

    def getLeft(self):
        return self.lchild

    def setLeft(self,ldata):
        self.lchild = Node(ldata)
        return self.lchild

    def getRight(self):
        return self.rchild  

    def setRight(self,rdata):
        self.rchild = Node(rdata)
        return self.rchild


class BST(object):
    """docstring for BST"""
    def __init__(self):
        self.root = None

    def insert(self,val):
        rt = self.root
        if rt is None:
            self.root = Node(val)
            return

        while rt:
            if rt.data >= val:
                if rt.getLeft() is None:
                    rt.setLeft(val)
                    return
                rt = rt.getLeft()
            elif rt.data < val:
                if rt.getRight() is None:
                    rt.setRight(val)
                    return
                rt = rt.getRight()
            else:
                rt.data = val

    def trave(self):
        stack = list()
        rt = self.root
        # 中序遍历
        while rt or stack:
            while rt:
                stack.append(rt)
                rt = rt.getLeft()
            rt = stack.pop()
            yield rt.data
            rt = rt.getRight()
        # # 后序遍历
        # while rt or stack:
        #     while rt:
        #         stack.append(rt)
        #         rt = rt.getRight()
        #     rt = stack.pop()
        #     yield rt.data
        #     rt = rt.getLeft()
        # # 前续遍历
        # while rt or stack:
        #     while rt:
        #         yield rt.data
        #         stack.append(rt)
        #         rt = rt.getLeft()
        #     rt = stack.pop()
        #     rt = rt.getRight()


if __name__ == '__main__':
    tree = BST()
    tree.insert(4)
    tree.insert(4)
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    tree.insert(1)
    tree.insert(7)
    tree.insert(6)
    tree.insert(100)
    tree.insert(97)
    for item in tree.trave():
        print(item)
