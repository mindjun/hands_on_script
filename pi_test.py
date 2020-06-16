# -*- coding: utf-8 -*-


def pi_calculate(n, res=1):
    if n == 1:
        return res
    else:
        # print('n is {}'.format(n))
        # print('here is {0} + {1}/{2} '.format(res,(-1)**((n-1) % 2)*1, (2*n-1)))
        return pi_calculate(n-1, res + (-1)**((n-1) % 2)*(1/(2*n-1)))


pi = pi_calculate(2) * 4
print(pi)


def pi_calculate1(n):
    init = 1
    if n == 1:
        return init
    for i in range(n):
        i += 1
        if i == 1:
            continue
        init = init + (-1)**(i-1) / (2*i - 1)

    return init

pi0 = pi_calculate1(2000000)*4
print(pi0)
