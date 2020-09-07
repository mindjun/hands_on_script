import time


# 2018.12.28 edit by jun.hu
def get_last4_mobile_number_sha256(mobile_number):
    """
    获取手机号最后四位的入库保存值
    规则: 使用前三位手机号 MD5 值作为密钥 + 手机号后四位 作 hmac_sha256
    hmac_sha256(md5(mobile_number[:3]), mobile_number[-4:])
    :param:
        * mobile_number: (string) 手机号
    :return:
    """
    time.sleep(1)
    return mobile_number[:4]


class Timer(object):
    def __init__(self, start=None):
        self.start = start if start else time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time()
        self.cost = self.stop - self.start
        return exc_type is None


with Timer() as ti:
    get_last4_mobile_number_sha256('15312341234')
    get_last4_mobile_number_sha256('15312341234')

print(ti.cost)

from contextlib import contextmanager


class Timer1(object):
    def __init__(self, start=None):
        self.start = start if start else time.time()

    @contextmanager
    def __call__(self, *args, **kwargs):
        print('Timer1')
        yield
        self.cost = time.time() - self.start


t = Timer1()
with t() as t0:
    get_last4_mobile_number_sha256('15312341234')
    get_last4_mobile_number_sha256('15312341234')
print(t.cost)


@contextmanager
def timer(start=None):
    start = start if start else time.time()
    print('timer')
    yield
    print(time.time() - start)


with timer() as t1:
    get_last4_mobile_number_sha256('15312341234')
    get_last4_mobile_number_sha256('15312341234')

from functools import wraps


def dec_test(info):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('start')
            print('dec args is {}'.format(info))
            func(*args, **kwargs)

        return wrapper

    return decorator


@dec_test('dec_test')
def func_1(a, b):
    print('here is func, args is {}, {}'.format(a, b))


func_1(1, 2)
