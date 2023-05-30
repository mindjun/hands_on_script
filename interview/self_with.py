from socket import socket, AF_INET, SOCK_STREAM
from functools import partial
import time
from contextlib import contextmanager


class MyWith(object):
    """
    with test
    """
    def __init__(self):
        print("__init__ method")

    def __enter__(self):
        print("__enter__ method")
        return self  # 返回对象给as后的变量

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("__exit__ method")
        if exc_traceback is None:
            print("Exited without Exception")
            return True
        else:
            print("Exited with Exception")
            return False

    def fun(self):
        print(self.__doc__)
        print('here is with fun')


def with_test():
    with MyWith() as my_with:
        print("running my_with")
        my_with.fun()
    print("------分割线-----")


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


# conn = LazyConnection(('www.python.org', 80))
# # Connection closed
# with conn as s:
#     # conn.__enter__() executes: connection open
#     s.send(b'GET /index.html HTTP/1.0\r\n')
#     s.send(b'Host: www.python.org\r\n')
#     s.send(b'\r\n')
#     # 在 iter 最后加一个 '' 作为结束标志
#     resp = b''.join(iter(partial(s.recv, 8192), b''))
#     # conn.__exit__() executes: connection closed
#     print(resp)


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


# Example use
with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1

if __name__ == '__main__':
    with_test()
