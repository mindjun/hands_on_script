import warnings


def my_demo1(a):
    return a*a


def my_demo(a):
    warnings.simplefilter('always')
    warnings.warn('my_demo is deprecated, and in 2.x it will stop working. Use my_demo1 instead.',
                  DeprecationWarning, stacklevel=2)
    return my_demo1(a)


print(my_demo(12))

