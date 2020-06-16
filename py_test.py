import pytest


def f():
    raise TypeError


def test_f():
    with pytest.raises(TimeoutError):
        f()


if __name__ == '__main__':
    pytest.main('-s')
