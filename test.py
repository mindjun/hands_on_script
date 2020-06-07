

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


# dp[i][j] = min(dp[i-1][j-1], dp[i-1][j] + 1, dp[i][j-1] + 1)
def min_distance(str1, str2):
    size1, size2 = len(str1), len(str2)
    dp = [[(size1 + size2) for _ in range(size2+1)] for _ in range(size1+1)]

    for i in range(size1+1):
        dp[i][0] = i
    for j in range(size2+1):
        dp[0][j] = j

    print(dp)

    for i in range(1, size1+1):
        for j in range(1, size2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    print(dp)
    return dp[-1][-1]


# abcd->eebcc
print(min_distance('abcd', 'eebcc'))


# 0 1 2 3
# 1
# 2
# 3