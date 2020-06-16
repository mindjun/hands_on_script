import random


class Node(object):
    def __init__(self, val, sub=None):
        self.val = val
        self.sub = sub

    def __repr__(self):
        return str(self.val)

    def add_sub(self, sub_node):
        self.sub = sub_node


def pop_item():
    head = Node(0)
    first = head
    for i in range(1, 10):
        new_node = Node(i)
        head.add_sub(new_node)
        head = new_node

    head.add_sub(first)

    count = 0

    while first.sub:
        pre = first
        first = first.sub
        count += 1

        if count % 3 == 0:
            print(f'pop {first}')
            pre.sub = first.sub
            if first.val == first.sub.val:
                break
            first = first.sub
            count = 0

    # print(f'pop {first}')


pop_item()


def select_sort(list1):
    i = 0
    while i < len(list1) - 1:
        j = i + 1
        min_index = i
        while j < len(list1):
            if list1[j] < list1[min_index]:
                min_index = j
            j += 1
        if i != min_index:
            list1[i], list1[min_index] = list1[min_index], list1[i]
        i += 1


def bubble_sort(list1):
    n = len(list1)
    while n > 1:
        i = 1
        swap = False
        while i < n:
            if list1[i] < list1[i-1]:
                list1[i], list1[i-1] = list1[i-1], list1[i]
                swap = True
            i += 1
        n -= 1
        if not swap:
            return


# test_list = [random.randint(1, 50) for _ in range(20)]
# print(test_list)
# bubble_sort(test_list)
# print(test_list)
