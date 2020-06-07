#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Node(object):
    def __init__(self, data):
        self._data = data
        self._next = None

    def getItem(self):
        return self._data

    def setItem(self, new_data):
        self._data = new_data
        return new_data

    def getnext(self):
        return self._next

    def setnext(self, node):
        if not isinstance(node, Node):
            return 'error type!'
        else:
            self._next = node
            return self._next


class Linked(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        """
        是否为空
        """
        return self._head is None

    def size(self):
        current = self._head
        count = 0
        while current:
            count += 1
            current = current.getnext()
        return count

    def add(self, item):
        """
        在链表首部添加
        """
        new_head = Node(item)
        new_head.setnext(self._head)
        self._head = new_head

    def append(self, item):
        """
        在链表尾部添加
        """
        new_tail = Node(item)
        if self.is_empty():
            self._head = new_tail
        else:
            current = self._head
            while current.getnext():
                current = current.getnext()
            current.setnext(new_tail)

    def search(self, item):
        current = self._head
        while current:
            if current.getItem() == item:
                return True
            else:
                current = current.getnext()
        return False

    def index(self, item):
        current = self._head
        count = 0
        founditem = False
        while current != None and not founditem:
            count += 1
            if current.getItem() == item:
                founditem = True
            else:
                current = current.getnext()
        if founditem:
            return count
        else:
            raise ValueError('%s is not in linkedlist' % item)

    def remove(self, item):
        current = self._head
        prenode = None
        while current != None:
            if current.getItem() == item:
                if not prenode:
                    self._head = current.getnext()
                else:
                    prenode.setnext(current.getnext())
                return current
            else:
                prenode = current
                current = current.getnext()

    def insert(self, pos, item):
        if pos <= 1:
            self.add(item)
        elif pos > self.size():
            self.append(item)
        else:
            newnode = Node(item)
            prenode = None
            current = self._head
            count = 1
            while count < pos:
                count += 1
                prenode = current
                current = current.getnext()
            prenode.setnext(newnode)
            newnode.setnext(current)

    def travel(self):
        current = self._head
        while not current:
            print(current, current.getItem())
            current = current.getnext()


if __name__ == '__main__':
    a = Linked()
    for i in range(1, 10):
        a.append(i)
    print(a.travel())
    print(a.search(6))
    print(a.index(3))
    a.remove(4)
    print(a.travel())
    a.insert(4, 10)
    print(a.travel())


class UnorderedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def getHead(self):
        return self.head

    def isEmpty(self):
        return self.head is None and self.tail is None

    def add(self, item):
        node = ListNode(item)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node  # the head is the most recently added node

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def append(self, item):
        node = ListNode(item)
        self.tail.setNext(node)
        self.tail = node

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if current.getNext() is None:
            self.tail = previous

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
