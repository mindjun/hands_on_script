import os


def path_travel(path):
    for item in os.listdir(path):
        temp_path = os.path.join(path, item)
        if os.path.isdir(temp_path):
            yield from path_travel(temp_path)
        else:
            yield os.path.join(path, item)


iter_travel = path_travel('/Users/jun.hu/PycharmProjects/hands_on_script/interview')
for item in iter_travel:
    print(item)


def minimize():
    print('entering')
    current = yield
    while True:
        print(f'get current: {current}')
        value = yield current
        print('returning')
        current = min(value, current)


def generator1():
    for i in range(5):
        yield i


def generator2(input_gen):
    for i in input_gen:
        yield i * 2


if __name__ == '__main__':
    it = minimize()
    next(it)
    print(it.send(1))
    print(it.send(10))
    print(it.send(4))
    print(it.send(-1))
    print(it.send(0))

    for result in generator2(generator1()):
        print(result)
