from stack.arrays import Array
from stack.abstractstack import AbstrackStack


class ArrayStack(AbstrackStack):

    # Class variable
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstrackStack.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def peek(self):
        if self.isEmpty():
            raise KeyError('this stack is empty')
        return self._items[len(self)-1]

    def push(self, item):
        if len(self) == ArrayStack.DEFAULT_CAPACITY:
            new_items = Array(ArrayStack.DEFAULT_CAPACITY*2)
            for i in range(len(self)):
                new_items[i] = self._items[i]
            self._items = new_items
        self._items[len(self)] = item
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError('this stack is empty')
        oldItem = self._items[len(self)-1]
        self._size -= 1
        return oldItem

    def clear(self):
        self._size = 0
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)

