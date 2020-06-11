

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

# 计算 1 至 n 中数字 x 出现的次数 x in range(0, 10)
# def count(n, x):
#     res, i = 0, 1
#
#     def helper(_n, _i):
#         len_str = len(str(_n))
#         if _i < 10:
#             return 1 if x < _i else 0
#         while True:
#             part_1 = pow(10, len_str)

# https://www.cnblogs.com/duanxz/p/9662862.html
def count(n, x):
    cnt, k, i = 0, n, 1
    while True:
        cnt += int(k / 10) * i
        cur = k % 10
        if cur > x:
            cnt += i
        elif cur == x:
            # 2500 -- 2593 ==> 94
            cnt += n % i + 1
        i *= 10
        k = int(n / i)
        if k < 10:
            break
    return cnt


print(count(2593, 5))
