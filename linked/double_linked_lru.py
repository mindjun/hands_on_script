"""
双向链表以及 LRU 的实现
"""

from collections import OrderedDict


class Node(object):
    def __init__(self, data, _pre=None, _next=None):
        self.data = data
        self.pre = _pre
        self.next = _next

    def __str__(self):
        return str(self.data)


class DoubleLink(object):
    def __init__(self):
        self.tail = None
        self.head = None
        self.capacity = 0

    def insert(self, data):
        if isinstance(data, Node):
            tmp_node = data
        else:
            tmp_node = Node(data)
        if self.capacity == 0:
            self.tail = tmp_node
            self.head = self.tail
        else:
            self.head.pre = tmp_node
            tmp_node.next = self.head
            self.head = tmp_node
        self.capacity += 1
        return tmp_node

    def remove(self, node):
        if node == self.head:
            self.head.next.pre = None
            self.head = self.head.next
        elif node == self.tail:
            self.tail.pre.next = None
            self.tail = self.tail.pre
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
        self.capacity -= 1

    def __str__(self):
        str_text = ""
        cur_node = self.head
        while cur_node:
            str_text += cur_node.data + " "
            cur_node = cur_node.next
        return str_text


class LRU(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.link = DoubleLink()

    def get(self, key):
        tmp_node = self.cache.get(key)
        self.link.remove(tmp_node)
        self.link.insert(tmp_node)
        return tmp_node.data

    def set(self, key, value):
        # 只有当 key 不存在 cache 中并且 capacity 达到上限才进行删除
        if key not in self.cache and self.capacity == self.link.capacity:
            self.link.remove(self.link.tail)

        # key 存在 cache 中的时候只需要更新 update，即是先删除再添加到链表头部
        if key in self.cache:
            self.link.remove(self.cache.get(key))

        tmp_node = self.link.insert(value)
        self.cache[key] = tmp_node


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        if self.capacity == len(self.cache):
            self.cache.popitem(last=False)
        self.cache.update({key: value})

    def get(self, key):
        value = self.cache.get(key)
        self.cache.pop(key)
        self.cache.update({key: value})
        return value


if __name__ == '__main__':
    r = LRU(3)
    r.set("1", "1")
    r.set("2", "2")
    r.set("3", "3")
    r.set("2", "b")
    print(r.link)
    print(r.get("1"))
    r.set("4", "4")
    print(r.link)

    r = LRUCache(3)
    r.set("1", "1")
    r.set("2", "2")
    r.set("3", "3")
    r.set("2", "b")
    print(r.cache)
    print(r.get("1"))
    r.set("4", "4")
    print(r.cache)
