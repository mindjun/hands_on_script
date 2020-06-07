import time
from threading import Timer


def wait_and_print_async(msg):
    print('start')
    start = time.time()

    def callback():
        print(msg)
        print(time.time() - start)

    timer = Timer(1.0, callback)
    timer.start()


wait_and_print_async('wait')
