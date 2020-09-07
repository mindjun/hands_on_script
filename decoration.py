# -*- coding:utf-8 -*-

"""
计时器装饰器的用法
"""

import functools
import signal
import time


class TimeoutExcept(Exception):
    pass


def timeout(seconds, err_info='function call timeout'):
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(err_info)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wrapper

    return decorated


@timeout(1, 'Function slow; aborted')
def slaw_function():
    time.sleep(5)


if __name__ == '__main__':
    slaw_function()
