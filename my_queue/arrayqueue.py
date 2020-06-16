from my_queue.abstractcollection import AbstractCollection
from my_queue.arrays import Array


class ArrayQueue(AbstractCollection):
    DEFAULT_CAPACITY = 5

    def __init__(self, sourceCollection=None):
        self._head = self._rear = 0
        self._capacity = ArrayQueue.DEFAULT_CAPACITY
        self._items = Array(self._capacity)
        super(ArrayQueue, self).__init__(sourceCollection)

    def __iter__(self):
        index_list = self._get_index_list()
        for item in index_list:
            yield self._items[item]

    def _get_index_list(self):
        index_list = list()
        if self._rear < self._head:
            index_list.extend(range(self._head, self._capacity))
            index_list.extend(range(0, self._rear+1))
        else:
            index_list.extend(range(self._head, self._rear+1))
        return index_list

    def add(self, item):
        if self.isEmpty():
            self._items[0] = item
            self._size += 1
        elif len(self) == self._capacity:
            # 队列满的情况
            # resize my_queue
            index_list = self._get_index_list()
            # 需要重置 _head 和 _rear
            self._head, self._rear = 0, len(self)-1

            self._capacity += 5
            new_items = Array(self._capacity)

            for index,item1 in enumerate(index_list):
                new_items[index] = self._items[item1]
            self._items = new_items
            # add item
            self._add_helper(item)
        else:
            self._add_helper(item)

    def _add_helper(self, item):
        self._rear = 0 if self._rear == self._capacity - 1 else self._rear + 1
        self._items[self._rear] = item
        self._size += 1

    def peek(self):
        if self.isEmpty():
            raise KeyError('my_queue is empty')
        return self._items[self._head]

    def pop(self):
        if self.isEmpty():
            raise KeyError('my_queue is empty')
        oldItem = self._items[self._head]
        self._items[self._head] = None
        self._head = 0 if self._head == self._capacity - 1 else self._head + 1
        self._size -= 1
        return oldItem

    def clear(self):
        self._size, self._head, self._rear = [0]*3


def mytest():
    queue = ArrayQueue()
    # print("Length:", len(my_queue))
    # print("Empty:", my_queue.isEmpty())
    print("Push 1-5")
    for i in range(5):
        queue.add(i)
    # print("Peeking:", my_queue.peek())
    # print("Items (bottom to top):",  my_queue)
    # print("Length:", len(my_queue))
    # print("Empty:", my_queue.isEmpty())
    # theClone = ArrayQueue(my_queue)
    # print("Items in clone (bottom to top):",  theClone)
    # theClone.clear()

    # print("Length of clone after clear:",  len(theClone))

    print("Push 6")
    queue.add(6)
    print("after adjust len:", queue)

    # print("Popping items (top to bottom): ", end="")
    # while not my_queue.isEmpty():
    #     print(my_queue.pop(), end=" ")
    #
    # print("\nLength:", len(my_queue))
    # print("Empty:", my_queue.isEmpty())

    for i in range(3):
        print(queue.pop())

    queue.add(6)
    queue.add(6)
    queue.add(6)
    queue.add(6)
    queue.add(6)
    queue.add(6)

    print(queue)

    for i in range(20, 30):
        queue.add(i)

    print(len(queue))
    for i in range(5):
        print(queue.pop())
    print(queue)

    for i in range(30, 40):
        queue.add(i)
    print(queue)

if __name__ == '__main__':
    mytest()
