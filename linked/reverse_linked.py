"""
列表的翻转
"""


class Node(object):
    def __init__(self, val, ne=None):
        self.data = val
        self.next = ne
        self.val = val

    def set_next(self, node):
        self.next = node


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_linked(head):
    """
    1 ==> 2 ==> 3 ==> 4 ==> 5    5 ==> 4 ==> 3 ==> 2 ==> 1
    :param head:
    :return:
    """
    if head is None or head.next is None:
        return head
    current, pre = head, None
    while current:
        temp = current.next
        current.next = pre
        current, pre = temp, current
    return pre


def reverse_linked_1(head):
    """
    递归实现
    :param head:
    :return:
    """
    if head is None or head.next is None:
        return head
    last = reverse_linked_1(head.next)
    head.next.next = head
    head.next = None
    return last


def reverse_pre_n(head, n):
    """
    翻转链表前 n 个节点
    1 ==> 2 ==> 3 ==> 4 ==> 5    reverse_pre_n(head, 3)
    head = _head = 1  successor = 4  last = 3
    :param head:
    :param n:
    :return:
    """
    successor = None

    def reverse_help(_head, _n):
        # 记录 last 之后的那个元素
        nonlocal successor
        if _n == 1:
            successor = _head.next
            return _head
        last = reverse_help(_head.next, _n - 1)
        _head.next.next = _head
        _head.next = successor
        return last
    return reverse_help(head, n)


def reverse_between(head, m, n):
    """
    翻转链表的 m-n 个节点
    1 ==> 2 ==> 3 ==> 4 ==> 5 ==> None  n=4, m=2
    ==> 1 ==> 4 ==> 3 ==> 2 ==> 5 ==> None
    :param head:
    :param m:
    :param n:
    :return:
    """
    if m == 1:
        # 相当于反转前 n 个元素
        return reverse_pre_n(head, n)
    # 前进到反转的起点触发 base case
    head.next = reverse_between(head.next, m - 1, n - 1)
    return head


def every_two_reverse(head):
    """
    1 ==> 2 ==> 3 ==> 4 ==>5
    head  next  tmp
    2 ==> 1 ==> 4 ==> 5
          3 ==> 4
          3 is new_head
    :param head:
    :return:
    """
    if head is None or head.next is None:
        return
    new_head = head.next
    while head is not None and head.next is not None:
        next = head.next
        tmp = next.next
        if tmp is None:
            # 节点数为偶数的情况
            next.next = head
            head.next = None
            break
        else:
            # 节点数为奇数的情况
            if tmp.next is None:
                head.next = tmp
            else:
                head.next = tmp.next
            next.next = head
            head = tmp
    return new_head


def reverse_linked3(head, tail):
    """
    :param head:
    :param tail:
    :return:
    """
    if head is None or head.next is None:
        return head
    current, pre = head, None
    while current.data != tail.data:
        temp = current.next
        current.next = pre
        current, pre = temp, current
    return pre


def reverse_group(head, k):
    """
    k 个一组翻转链表
    https://labuladong.gitbook.io/algo/gao-pin-mian-shi-xi-lie/k-ge-yi-zu-fan-zhuan-lian-biao
    :param head:
    :param k:
    :return:
    """
    p1, p2 = head, head
    for i in range(k):
        # 不足 k 个元素，直接返回
        if not p2:
            return head
        p2 = p2.next
    # 翻转 p1 - p2 的元素
    new_head = reverse_linked3(p1, p2)
    p1.next = reverse_group(p2, k)
    return new_head


def check_is_loop_in_linked_and_find_entry(head):
    """
    检查链表中是否有环，快慢指针实现
    :param head:
    :return:
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow.data == fast.data:
            slow2 = head
            while slow.data != slow2.data:
                slow = slow.next
                slow2 = slow2.next
            return slow2.data
    return False


def sort_linked(head):
    """
    归并排序
    :param head:
    :return:
    """
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 这里就是拆分为两部分的过程
    mid, slow.next = slow.next, None
    left, right = sort_linked(head), sort_linked(mid)
    result = temp_head = Node(0)

    while left and right:
        if left.data < right.data:
            temp_head.next = left
            left = left.next
        else:
            temp_head.next = right
            right = right.next
        temp_head = temp_head.next

    temp_head.next = left if left else right
    return result.next


def sort_linked1(_head, _end=None):
    """
    快速排序
    :param _head:
    :param _end:
    :return:
    """
    if not _head or not _head .next:
        return _head

    def helper(head, end):
        p1, p2 = head, head
        while p2 != end:
            if p2.data < head.data:
                p1 = p1.next
                p1.data, p2.data = p2.data, p1.data
            p2 = p2.next
        p1.data, head.data = head.data, p1.data
        return p1

    def sort(head, end):
        if head == end or head.next == end:
            return head
        node = helper(head, end)
        sort(head, node)
        sort(node.next, end)

    sort(_head, _end)
    return _head


# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
def remove_duplicate(head):
    """
    删除重复的节点
    节点已经是升序
    :param head:
    :return:
    """
    node = head
    while head and head.next:
        if head.data == head.next.data:
            head.next = head.next.next
        else:
            head = head.next
    return node


# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
def delete_duplicate(head):
    """
    删除所有包含重复数字的节点
    节点已经是升序
    :param head:
    :return:
    """
    thead = ListNode('0')
    thead.next = head
    node = thead
    while thead.next:
        left = right = thead.next
        # left right 指针不断移动，直到不想等为止
        while right.next and right.next.val == left.val:
            right = right.next
        if left == right:
            thead = thead.next
        else:
            thead.next = right.next
    return node.next


# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
def delete_duplicate_(head):
    """
    删除所有包含重复数字的节点，递归解法
    节点已经是升序
    :param head:
    :return:
    """
    if not head:
        return head
    # 找到相同的数
    if head.next and head.val == head.next.val:
        while head.next and head.val == head.next.val:
            head = head.next
        # 从下一个不相同的数开始递归
        return delete_duplicate_(head.next)
    else:
        head.next = delete_duplicate_(head.next)
    return head


if __name__ == '__main__':
    # _h = Node(1, Node(1, Node(3, Node(4, Node(4, Node(6, Node(7)))))))
    # _h = Node(1, Node(1, Node(2, Node(2, Node(2)))))
    # [1, 2, 3, 3, 4, 4, 5]
    _h = Node(1, Node(2, Node(3, Node(3, Node(4, Node(4, Node(5)))))))

    res = delete_duplicate_(_h)

    remove_res = remove_duplicate(_h)
    while remove_res:
        print(remove_res.data)
        remove_res = remove_res.next

    import copy
    h = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))

    res = reverse_between(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7))))))), 2, 4)
    sort_arg = copy.deepcopy(res)
    sort_arg1 = copy.deepcopy(res)

    reverse_res = list()
    while res:
        reverse_res.append(res.data)
        res = res.next
    print(reverse_res)

    # sort list
    sort_res = sort_linked(sort_arg)
    sort_result = list()
    while sort_res:
        sort_result.append(sort_res.data)
        sort_res = sort_res.next

    print('归并排序： ')
    print(sort_result)

    # sort list
    h3 = Node(5, Node(1, Node(2, Node(6, Node(4, Node(7, Node(3)))))))
    sort_res1 = sort_linked1(sort_arg1)
    sort_result = list()
    while sort_res1:
        sort_result.append(sort_res1.data)
        sort_res1 = sort_res1.next

    print('快速排序： ')
    print(sort_result)

    every_two_reverse_list = list()
    new_h = every_two_reverse(h)
    while new_h:
        every_two_reverse_list.append(new_h.data)
        new_h = new_h.next

    print(f'every_two_reverse_list is {every_two_reverse_list}')
    assert every_two_reverse_list == [2, 1, 4, 3, 6, 5, 7]

    h4 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
    reverse_group_res = reverse_group(h4, 2)
    reverse_group_list = list()
    while reverse_group_res:
        reverse_group_list.append(reverse_group_res.data)
        reverse_group_res = reverse_group_res.next
    print(f'reverse_group(head, 2) is {reverse_group_list}')

    h = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
    reverse_list = list()
    new_h_1 = reverse_linked(h)
    while new_h_1:
        reverse_list.append(new_h_1.data)
        new_h_1 = new_h_1.next
    print(reverse_list)
    assert reverse_list == [7, 6, 5, 4, 3, 2, 1]

    h = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
    reverse_list2 = list()
    new_h_2 = reverse_linked_1(h)
    while new_h_2:
        reverse_list2.append(new_h_2.data)
        new_h_2 = new_h_2.next

    print(reverse_list2)

    a, b, c, d, e, f, g, h = [Node(i) for i in 'abcdefgh']
    # 生成一个环
    g.set_next(e)
    f.set_next(g)
    e.set_next(f)
    d.set_next(e)
    c.set_next(d)
    b.set_next(c)
    a.set_next(b)
    h.set_next(a)

    print(check_is_loop_in_linked_and_find_entry(h))


# ListNode reverse(ListNode head) {
#     if (head.next == null) return head;
#     ListNode last = reverse(head.next);
#     head.next.next = head;
#     head.next = null;
#     return last;
# }
