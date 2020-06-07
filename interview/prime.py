import math
from functools import lru_cache


@lru_cache(maxsize=10)
def is_prime(n):
    print('cal num : {}'.format(n))
    for i in range(2, int(math.ceil(n/2))):
        if n % i == 0:
            return False, i
    return True, n


def prime_divide(num):
    result = list()
    while not is_prime(num)[0]:
        result.append(is_prime(num)[1])
        num = int(num/is_prime(num)[1])
    result.append(num)
    print(result)


prime_divide(212955649)


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


from collections import Counter
print(dict(Counter([1,2,3,4,5,8,9,0,12,3,5])))
