import multiprocessing
import threading

poll = multiprocessing.Pool()


def test(a):
    pass


p = multiprocessing.Process(target=test, args=(1,))
p.start()
p.join()

multiprocessing.cpu_count()

t = threading.Thread(target=test, args=(1, ))
t.start()
t.join()
