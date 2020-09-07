from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('./somefile.txt') as f:
    _lines = linehistory(f)
    for line in _lines:
        if 'python' in line:
            for _lineno, _hline in _lines.history:
                print('{}:{}'.format(_lineno, _hline), end='')
