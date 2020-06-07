def singleton(cls):
    # 装饰器实现
    instance = dict()

    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper


@singleton
class Test(object):
    def __init__(self):
        pass


t2 = Test()
t1 = Test()

print(id(t1))
print(id(t2))


# 使用 __new__ 方法
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


# 共享属性，创建实例时把所有实例的__dict__都指向同一个字典，这样他们具有相同的属性方法
class Borg(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Borg, cls)
        ob.__dict__ = cls._state
        return ob


# 另外，使用import方法也能实现单例

class Singleton1(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


# Example
class Spam(metaclass=Singleton1):
    def __init__(self):
        print('Creating Spam')
