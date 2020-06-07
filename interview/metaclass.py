# -*- coding:utf-8 -*-

"""
元类（metaclass）的演示实例
使用元类，拦截一个类的创建，将其属性全部修改为大写，然后返回修改之后的类
"""


# 请记住，'type'实际上是一个类，就像'str'和'int'一样
# 所以，你可以从type继承
class UpperAttrMetaclass0(type):
    """
    # __new__ 是在 __init__ 之前被调用的特殊方法
    # __new__ 是用来创建对象并返回它的方法
    #     # 而 __init__ 只是用来将传入的参数初始化给对象
    # 你很少用到 __new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写 __new__
    # 如果你希望的话，你也可以在 __init__ 中做些事情
    # 还有一些高级的用法会涉及到改写 __call__ 特殊方法，但是我们这里不用
    """
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        # upperattr_metaclass 相当于 self， 每一个实例方法的第一个参数都是类的实例
        upper_attr = {}
        for name, val in future_class_attr:
            if not name.startswith('__'):
                upper_attr[name.upper()] = val
            else:
                upper_attr[name] = val
        # 使用type来创建新的类
        # return type(future_class_name, future_class_parents, future_class_attr)

        # 重用 type.__new__ 方法
        # 这就是基本的 OOP 编程，没什么魔法
        return type.__new__(upperattr_metaclass, future_class_name,
                            future_class_parents, upper_attr)


# 简写如下
class UpperAttrMetaclass(type):
    def __new__(cls, class_name, bases, dct):
        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, class_name, bases, uppercase_attr)


# 元类会自动将你通常传给'type'的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
    返回一个将属性列表变为大写字母的类对象
    """
    # 选取所有不以'__'开头的属性,并把它们编程大写
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val

    # 用'type'创建类
    return type(future_class_name, future_class_parents, uppercase_attr)


# UpperAttrMetaclass0和upper_attr以及UpperAttrMetaclass都可用

# python2 的写法
# 将会影响整个模块
# __metaclass__ = UpperAttrMetaclass
# class Foo():
#     bar = 'foo'


# python3 的写法
class Foo(object, metaclass=upper_attr):
    bar = 'foo'


# 使用元类实现单例
class SigleInstance(type):
    """
    实现单列模式的元类
    总之，metaclass的主要任务是：
    拦截类，
    修改类，
    返回类
    """

    def __init__(cls, classname, parrentstuple, attrdict):
        """
        """
        super(SigleInstance, cls).__init__(classname, parrentstuple, attrdict)
        cls._instance = None

    def __call__(self, *args, **kargs):
        """
        """
        if self._instance:
            return self._instance
        else:
            self._instance = super(SigleInstance, self).__call__(*args, **kargs)
            return self._instance


class Earth(object, metaclass=SigleInstance):

    def __init__(self,a,b):
        self.a = a
        self.b = b


if __name__ == '__main__':
    print(hasattr(Foo, 'bar'))
    # 输出: False
    print(hasattr(Foo, 'BAR'))
    # 输出: True

    f = Foo()
    print(f.BAR)
    # 输出: 'bip'

    e1 = Earth(1,2)
    e2 = Earth(3,2)

    print(id(e1))
    print(id(e2))
