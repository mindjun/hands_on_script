
from stack.node import Node
from stack.abstractstack import AbstrackStack


class LinkedStack(AbstrackStack):
    def __init__(self, sourceCollection=None):
        # self._items 总是指向顶端元素
        self._items = None
        AbstrackStack.__init__(self, sourceCollection)

    def __iter__(self):
        def visitNonde(node):
            if node is not None:
                visitNonde(node.next)
                tempList.append(node.data)

        tempList = list()
        visitNonde(self._items)
        return iter(tempList)

    def peek(self):
        if self.isEmpty():
            raise KeyError('the stack is Empty')
        return self._items.data

    def clear(self):
        self._items = None
        self._size = 0

    def pop(self):
        if self.isEmpty():
            raise KeyError('the stack is Empty')
        oldItem = self._items.data
        self._items = self._items.next
        self._size -= 1
        return oldItem

    def push(self, item):
        # 在顶端添加
        self._items = Node(item, self._items)
        self._size += 1

if __name__ == '__main__':
    pass