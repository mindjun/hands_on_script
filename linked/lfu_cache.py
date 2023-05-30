from collections import defaultdict

class Node(object):
    def __init__(self, val=-1, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.next = nxt

    def __str__(self):
        return str(self.val)

    def set(self, val):
        self.val = val


class DoubleLink(object):
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def insert(self, data):
        if isinstance(data, Node):
            temp_node = data
        else:
            temp_node = Node(data)

        if self.head is None:
            self.tail = self.head = temp_node
        else:
            temp_node.pre = self.tail
            self.tail.next = temp_node
            self.tail = temp_node
        self.size += 1
        return temp_node

    def remove(self, node):
        # 只有一个节点的时候，直接清空
        if self.size == 1:
            self.head = self.tail = None
        elif node == self.head:
            self.head.next.pre = None
            self.head = self.head.next
        elif node == self.tail:
            self.tail.pre.next = None
            self.tail = self.tail.pre
        else:
            node.pre.next = node.next
            node.next.pre = node.pre

        self.size -= 1

    def is_empty(self):
        if self.size == 0:
            empty = False
        else:
            empty = True
        return empty

class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.key2val = dict()
        self.key2freq = defaultdict(int)
        self.freq2link = defaultdict(DoubleLink)
        self.key2node = defaultdict(Node)
        # todo 增加 freq2key,方便根据 freq 去删除数据
        self.min_freq = 0

    def get(self, key):
        if key not in self.key2val:
            return -1
        val = self.key2val.get(key)
        self.increase_freq(key, val)
        return val

    def put(self, key, val):
        if key not in self.key2val and len(self.key2val) == self.capacity:
            # 删除
            self.delete_min_freq_data()

        # 没有就新建，否则更新
        old_val = self.key2val.get(key)
        if old_val is None:
            # 没有，新建
            self.key2val[key] = val
        else:
            # 存在，更新node
            node = self.key2node.get(key)
            node.set(val)
        self.increase_freq(key, val)

    def delete_min_freq_data(self):
        double_link = self.freq2link.get(self.min_freq)
        double_link.remove(double_link.head)

    def increase_freq(self, key, val):
        last_freq = self.key2freq[key]
        freq = last_freq + 1
        self.key2freq[key] = freq
        # last_double_link 刪除 node，如果 last_freq 为 0，就不用删除原来的 node，直接新加
        node = None
        if last_freq != 0:
            last_double_link = self.freq2link.get(last_freq)
            node = self.key2node.get(key)
            last_double_link.remove(node)
            if last_double_link.size == 0:
                self.freq2link.pop(last_freq)

        node = node if node else val
        # 往新的 double_link 增加 node
        double_link = self.freq2link[freq]
        temp_node = double_link.insert(node)
        self.key2node[key] = temp_node
        self.update_min_freq()

    def update_min_freq(self):
        # todo 在O(1)的时间复杂度内，计算出 min_freq
        self.min_freq = min(list(self.freq2link.keys()))


if __name__ == '__main__':
    lfu = LFUCache(3)
    lfu.put(1, '1')
    lfu.put(2, '2')
    lfu.put(3, '3')
    lfu.put(2, '22')
    lfu.put(4, '4')
    print('here')

