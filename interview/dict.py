"""
用字典的值进行排序
"""
import operator

x = {1: 2, 3: 4, 4:3, 2:1, 0:0}

sorted_x = sorted(x.items(), key=operator.itemgetter(1))

sorted_y = sorted(x.items(), key=operator.itemgetter(0))

print(sorted_x)
print(sorted_y)

print(sorted(x.items(), key=lambda y:y[1]))


if 1 in x.keys():
    print('in')
else:
    print('not in')

# 字典生成式
d = {key:value for key,value in enumerate(range(10),2)}

print(d)

# __missing__ 方法
# http://kodango.com/understand-defaultdict-in-python
# defaultdict 可以看出当使用 __getitem__() 方法访问一个不存在的键时(dict[key]这种形式实际上是
# __getitem__()方法的简化形式)，会调用__missing__()方法获取默认值，并将该键添加到字典中去。


class Defaulting(dict):
    def __missing__(self, key):
        self[key] = 'default'
        return 'default'


de = Defaulting()
print(de['test'])

print(de)
