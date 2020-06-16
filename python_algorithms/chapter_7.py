from heapq import heapify, heappop, heappush
from itertools import count


def huffman(seq, frq):
    num = count()
    trees = list(zip(frq, num, seq))
    heapify(trees)
    while len(trees) > 1:
        fa, _, a = heappop(trees)
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa+fb, n, [a,b]))
    # print(trees)
    return trees[0][-1]


seq_ = 'abcdefghi'
frq_ = [4,5,6,9,11,12,15,16,20]
# print(huffman(seq_, frq_))


def codes(trees, prefix=''):
    if len(trees) == 1:
        print(trees, prefix)
        yield (trees, prefix)
        return
    for bit, child in zip("01", trees):
        for pair in codes(child, prefix+bit):
            print(pair)
            yield pair


# print(list(codes(huffman(seq_, frq_))))

import random
import string
from collections import Counter
str1 = ''.join([random.choice(string.ascii_lowercase) for i in range(100)])
print(str1)
res1 = Counter(str1)
keys = list()
values = list()

for key,value in res1.items():
    keys.append(key)
    values.append(value)

print(keys)
print(values)


