# -*- coding: utf8 -*-


class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class TwoWayNode(Node):
    def __init__(self, data, previous = None, next = None):
        super(TwoWayNode, self).__init__(data,next)
        self.previous = previous


class LinkedBag(object):
    def __init__(self, sourceCollection = None):
        self._head = None
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def add(self, item):
        self._head = Node(item, self._head)
        self._size += 1

    def __len__(self):
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __iter__(self):
        cursor = self._head
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return '{' + ', '.join(map(str, self)) + '}'

    def __add__(self, other):
        # for operate +
        result = LinkedBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        if self is other:
            return False
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if item not in other:
                return False
        return True
        
    def remove(self, item):
        if item not in self:
            raise KeyError(str(item) + 'not in bag')
        
        # 需要记录目标节点前一个节点pre，查找到目标节点后设置 pre.next = target.next 即可
        pre = None
        target = self._head
        for targetitem in self:
            if targetitem == item:
                break
            pre = target
            target = target.next
        
        # 如果是头结点
        if target == self._head:
            self._head = self._head.next
        else:
            pre.next = target.next
        self._size -= 1
    
    def clear(self):
        self._head = None
        self._size = 0


class TwoWayLinkedBag(LinkedBag):
    def __init__(self, sourceCollection = None):
        self._head = None
        self._size = 0
        # 添加一个tail节点
        self._tail = None
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def add(self, item):
        if self._head is None:
            # 如果为空链表，设置头尾一致
            self._head = TwoWayNode(item)
            self._tail = self._head
        else:
            self._tail.next = TwoWayNode(item, self._tail, None)
            self._tail = self._tail.next
        self._size += 1

    def __add__(self, other):
        # for operate +
        result = TwoWayLinkedBag(self)
        for item in other:
            result.add(item)
        return result

    def clear(self):
        self._head = self._tail = None
        self._size = 0

    def remove(self, item):
        if item not in self:
            raise KeyError(str(item) + ' not in bag')

        target = None
        for targetitem in self:
            if targetitem == item:
                target = self._head
                break
            target = targetitem.next
        if len(self) == 1:
            self._head = self._tail = None
        # 如果是第一个节点
        elif target == self._head:
            self._head = self._head.next
            self._head.previous = None
        elif target == self._tail:
        # 如果是末尾节点
            self._tail.previous = None
        else:
            target.previous.next = target.next
            target.next.previous = target.previous
        self._size -= 1


def mytest(bagType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    lyst = [2013, 61, 1973]
    print("The list of items added is:", lyst)
    b1 = bagType(lyst)
    print("Expect 3:", len(b1))
    print("Expect the bag's string:", b1)
    print("Expect True:", 2013 in b1)
    print("Expect False:", 2012 in b1)
    print("Expect the items on separate lines:")
    for item in b1:
        print(item)
    b1.clear()
    print("Expect {}:", b1)
    b1.add(25)
    b1.remove(25)
    print("Expect {}:", b1)
    b1 = bagType(lyst)
    b2 = bagType(b1)
    print("Expect True:", b1 == b2)
    print("Expect False:", b1 is b2)
    print("Expect two of each item:", b1 + b2)
    for item in lyst:
        b1.remove(item)
    print("Expect {}:", b1)
    print("Expect crash with KeyError:")
    b2.remove(99)


if __name__ == '__main__':
    mytest(TwoWayLinkedBag)
