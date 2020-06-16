# -*- coding:utf-8 -*-
"""
装饰器, win下signal模块缺少属性
"""
import time
import signal
import functools
from functools import wraps


class TimeoutError(Exception): pass


def timeout(seconds, error_message='Function call timed out'):
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return functools.wraps(func)(wrapper)

    return decorated


@timeout(1, 'Function slow; aborted')
def slow_function():
    print('start')
    time.sleep(5)


# slow_function()


# 装饰器用在缓存
def memo(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper


@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


class MyappSelf(object):
    def __init__(self):
        self.fuc_map = {}

    def register_outer(self, url):
        def register(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                print('func {} register'.format(fn.__name__))
                fn_dict = dict()
                fn_dict['args'] = args
                fn_dict['kwargs'] = kwargs
                fn_dict['name'] = fn.__name__
                self.fuc_map[url] = fn_dict
            return wrapper
        return register

    def __call__(self, *args, **kwargs):
        print('call')
        if 'GET' in kwargs:
            print('get method')
        elif 'POST' in kwargs:
            print('post method')
        else:
            print('other method')


selfapp = MyappSelf()


@selfapp.register_outer('/')  # register
# main_page = register(main_page)
def main_page(method='POST'):
    print(method)
    print('main page with post')
    return 'This is the main page.'


print(main_page(method='GET'))
print(selfapp.fuc_map)


class MyApp(object):
    def __init__(self):
        self.func_map = {}

    def register(self, name):
        def func_wrapper(func):
            self.func_map[name] = func
            return func

        return func_wrapper

    def call_method(self, name=None):
        print(name)
        func = self.func_map.get(name, None)
        if func is None:
            raise Exception("No function registered against - " + str(name))
        return func()


app = MyApp()


@app.register('/')
def main_page_func():
    return "This is the main page."


@app.register('/next_page')
def next_page_func():
    return "This is the next page."


print(app.call_method('/'))
print(app.call_method('/next_page'))

# 带有参数的装饰器
# https://coolshell.cn/articles/11265.html
import pymysql
import sys
from functools import wraps


class Configuraion:
    def __init__(self, env):
        if env == "Prod":
            self.host = "coolshell.cn"
            self.port = 3306
            self.db = "coolshell"
            self.user = "coolshell"
            self.passwd = "fuckgfw"
        elif env == "Test":
            self.host = 'localhost'
            self.port = 3300
            self.user = 'coolshell'
            self.db = 'coolshell'
            self.passwd = 'fuckgfw'


def mysql(sql):
    _conf = Configuraion(env="Prod")

    def on_sql_error(err):
        print(err)
        sys.exit(-1)

    def handle_sql_result(rs):
        if rs.rows > 0:
            fieldnames = [f[0] for f in rs.fields]
            return [dict(zip(fieldnames, r)) for r in rs.rows]
        else:
            return []

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            mysqlconn = pymysql.Connection()
            mysqlconn.settimeout(5)
            mysqlconn.connect(_conf.host, _conf.port, _conf.user,
                              _conf.passwd, _conf.db, True, 'utf8')
            try:
                rs = mysqlconn.query(sql, {})
            except pymysql.Error as e:
                on_sql_error(e)

            data = handle_sql_result(rs)
            kwargs["data"] = data
            result = fn(*args, **kwargs)
            mysqlconn.close()
            return result

        return wrapper

    return decorator


@mysql(sql="select * from coolshell")
def get_coolshell(data):
    pass


# 类装饰器

class MakeHtmlTagClass(object):
    # 先执行 init 再执行 call
    def __init__(self, tag, css_class=""):
        self._tag = tag
        self._css_class = " class='{0}'".format(css_class) \
            if css_class != "" else ""

    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            return "<" + self._tag + self._css_class + ">" \
                   + fn(*args, **kwargs) + "</" + self._tag + ">"

        return wrapped


@MakeHtmlTagClass(tag="b", css_class="bold_css")
@MakeHtmlTagClass(tag="i", css_class="italic_css")
def hello(name):
    return "Hello, {}".format(name)


print(hello("Hao Chen"))
