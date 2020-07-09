

# https://leetcode-cn.com/problems/triangle/
# dfs 解法，leetcode 超过时间限制
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
def minimum_total(triangle):
    min_sum = float('inf')
    path = list()
    result = list()

    def dfs(start_x, start_y, temp_res):
        if start_x == len(triangle) - 1:
            nonlocal min_sum
            min_sum = min(min_sum, temp_res + triangle[start_x][start_y])
            result.append(list(path))
            return

        path.append([start_x + 1, start_y])
        dfs(start_x + 1, start_y, temp_res + triangle[start_x][start_y])
        path.pop()

        path.append([start_x + 1, start_y + 1])
        dfs(start_x + 1, start_y + 1, temp_res + triangle[start_x][start_y])
        path.pop()

    dfs(0, 0, 0)
    print(result)
    for path_ in result:
        _temp_res = triangle[0][0]
        _path = f'{_temp_res}'
        for item in path_:
            _temp_res += triangle[item[0]][item[1]]
            _path += f' ==> {triangle[item[0]][item[1]]}'
        print(f'path {_path} sum is {_temp_res}')
    return min_sum


# 自顶向下
# 结果为 dp 最后一列中的最小值
def minimum_total_dp_top_down(triangle):
    dp = [[0] * len(triangle[i]) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 分为上一层没有左边值，没有右边值，正常的三种情况
            if j - 1 < 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j >= len(triangle[i]) - 1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

    print(f'minimum_total_dp is {dp}')
    return min(dp[-1])


# 自底向上
def minimum_total_with_cache(triangle):
    cache = [[-1] * len(triangle[i]) for i in range(len(triangle))]

    def dfs(x, y):
        if x == len(triangle):
            return 0

        if cache[x][y] != -1:
            return cache[x][y]
        cache[x][y] = min(dfs(x+1, y), dfs(x+1, y+1)) + triangle[x][y]
        return cache[x][y]

    res = dfs(0, 0)
    print(cache)
    return res


# 自底向上，与 cache 版本一致，先将 dp[-1] 这一行初始化为 triangle 的最后一行，我们要求的结果就在 dp[0][0]
# dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
def minimum_total_dp(triangle):
    dp = [[0] * len(triangle[i]) for i in range(len(triangle))]
    for index, item in enumerate(triangle[-1]):
        dp[-1][index] = item

    for i in range(len(triangle) - 1)[::-1]:
        for j in range(len(triangle[i])):
            dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
    print(f'minimum_total_dp is {dp}')
    return dp[0][0]


triangle_ = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
triangle__ = [
    [1],
    [-2, -5],
    [3, 6, 9],
    [-1, 2, 4, -3]]
print(minimum_total_with_cache(triangle__))
print(minimum_total_dp(triangle__))
print(minimum_total_dp_top_down(triangle__))
