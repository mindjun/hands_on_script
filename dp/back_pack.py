

# https://www.lintcode.com/problem/backpack/description
def _back_pack(m, weights):
    size = len(weights)
    # dp[i][j] 前 i 个物品，是否能装 j
    # dp[i][j] = dp[i-1][j] or dp[i-1][j-weights[i-1]]
    dp = [[0] * (m + 1) for _ in range(size + 1)]

    for i in range(size + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j]
                if j - weights[i-1] >= 0:
                    dp[i][j] = dp[i][j] or dp[i-1][j-weights[i-1]]
    # 找到能装满 size 的最大 j
    for j in range(m + 1)[::-1]:
        if dp[size][j]:
            return j
    return 0


print(_back_pack(10, [3, 4, 8, 5]))


# https://github.com/dashidhy/algorithm-pattern-python/blob/master/basic_algorithm/dp.md
def _back_pack_ii(m, weights):
    size = len(weights)

    dp = [0] * (m + 1)
    dp_new = [0] * (m + 1)

    for i in range(size):
        for j in range(1, m + 1):
            use_ai = 0 if j - weights[i] < 0 else dp[j-weights[i]] + weights[i]
            dp[j] = max(dp[j], use_ai)
        dp, dp_new = dp_new, dp
    return dp[-1]


print(_back_pack_ii(10, [3, 4, 8, 5]))


# 0-1 背包问题
# https://zhuanlan.zhihu.com/p/152166707
# dp[i][j] 定义为前 i 个物品放入空间大小为 j 时候占用的最大体积
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]] + nums[i])
def back_pack(m, weights, values):
    size = len(weights)
    dp = [[0] * (m + 1) for _ in range(size + 1)]

    for i in range(1, size + 1):
        for j in range(1, m + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


m_ = 15
weights_ = [3, 2, 6, 7, 1, 4, 9, 5]
values_ = [6, 3, 5, 8, 3, 1, 6, 9]
print(f'back_pack to m: {m_}, weights is {weights_}, values is {values_} ==> {back_pack(m_, weights_, values_)}')


# 使用滚动数组的优化，关键点在于倒序
def back_pack_ii(m, weights, values):
    f = [0] * (m + 1)
    for i in range(len(weights)):
        for j in range(weights[i], m + 1)[::-1]:
            f[j] = max(f[j], f[j - weights[i]] + values[i])

    return f[m]


print(f'back_pack_ii to m: {m_}, weights is {weights_}, values is {values_} ==> {back_pack_ii(m_, weights_, values_)}')


# https://zhuanlan.zhihu.com/p/35643721
# 完全背包问题，每种物品有无数多个
def full_back_pack(m, weights, values):
    f = [0] * (m + 1)
    for i in range(len(weights)):
        # 这里是和 0-1 背包的唯一区别，正序遍历
        for j in range(weights[i], m + 1):
            f[j] = max(f[j], f[j - weights[i]] + values[i])

    return f[m]
