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


# 0 1 2 3
# 1
# 2
# 3
