import math
from functools import lru_cache


def prime_divide_(num):
    res = list()
    while num != 1:
        ceil_num = int(math.ceil(num/2))
        for i in range(2, ceil_num):
            if num % i == 0:
                res.append(i)
                num = int(num / i)
                break
            if ceil_num - 1 == i:
                res.append(num)
                num = 1
                break
    return res
    # res = list()
    # while num != 1:
    #     for i in range(2, num+1):
    #         if num % i == 0:
    #             res.append(i)
    #             num = int(num / i)
    #             break
    # return res


print('prime_divide_ {}'.format(prime_divide_(212955649)))
print('prime_divide_ {}'.format(prime_divide_(90)))


@lru_cache(maxsize=10)
def is_prime(n):
    # print('cal num : {}'.format(n))
    for i in range(2, int(math.ceil(n/2))):
        if n % i == 0:
            return False, i
    return True, n


def prime_divide(num):
    result = list()
    # flag = False
    # while not flag:
    while num != 1:
        _, divided = is_prime(num)
        result.append(divided)
        num = int(num/divided)
    return result


print(f'prime_divide {prime_divide(212955649)}')
print(f'prime_divide {prime_divide(90)}')


@lru_cache(maxsize=10)
def my_prime_divide(num):
    temp_num = num
    for i in range(2, int(math.ceil(temp_num))):
        if temp_num % i == 0:
            prime_list.append(i)
            num = int(temp_num / i)
            break
    if num == temp_num:
        prime_list.append(num)
        return
    else:
        my_prime_divide(num)


prime_list = list()
my_prime_divide(12345678)
print(prime_list)


# 高效计算质数数量的方法
# https://leetcode-cn.com/problems/count-primes/
def count_primes_py(n):
    """
    求n以内的所有质数个数（纯python代码）
    """
    # 最小的质数是 2
    if n < 2:
        return 0

    _is_prime = [1] * n
    _is_prime[0] = _is_prime[1] = 0   # 0和1不是质数，先排除掉

    # 埃式筛，把不大于根号n的所有质数的倍数剔除
    for i in range(2, int(n ** 0.5) + 1):
        if _is_prime[i]:
            for j in range(i*i, n, i):
                _is_prime[j] = False
            # _is_prime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

    return sum(_is_prime)


print(count_primes_py(10))
