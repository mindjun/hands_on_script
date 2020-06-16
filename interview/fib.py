"""
台阶问题/斐波纳挈
"""


fib0 = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)


def memo(func):
    """
    装饰器，使用缓存，避免重复计算
    :param func:
    :return:
    """
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


@memo
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)


def fib1(n):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a+b


print(fib(10))
print(list(fib1(10)))


# 变态台阶问题
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法

fib2 = lambda n: n if n < 2 else 2*fib2(n-1)

print(fib2(10))
