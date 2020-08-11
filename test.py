# abc, 2 ==> aa, bb, cc, ab, ac, bd
def combine(str1, n):
    res = list()

    def helper(track):
        if len(track) == n:
            res.append(''.join(track))
            return

        for ch in str1:
            track.append(ch)
            helper(track)
            track.pop()

    _track = list()
    helper(_track)
    return res


# a ==> a  aa, ab, ac  [] b ==> ba bb bc
print(combine('abc', 3))


def my_func(num):
    if num < 10:
        return str(num)
    return str(num % 10) + my_func(num // 10)


print(my_func(1234))
print(type(my_func(1234)))


def is_valid(s):
    stack = list()
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return True if not stack else False


print(is_valid('(())'))
