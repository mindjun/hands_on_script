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
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j >= len(triangle[i]) - 1:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

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
        cache[x][y] = min(dfs(x + 1, y), dfs(x + 1, y + 1)) + triangle[x][y]
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
            dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
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
print(minimum_total(triangle__))
print(minimum_total_with_cache(triangle__))
print(minimum_total_dp(triangle__))
print(minimum_total_dp_top_down(triangle__))


# https://leetcode-cn.com/problems/minimum-path-sum/
# 自底向上
def min_path_sum_cache(nums):
    cache = [[-1] * (len(nums[0]) + 1) for _ in range(len(nums) + 1)]

    def dfs(x, y):
        if x == len(nums) - 1 and y == len(nums[-1]) - 1:
            return nums[-1][-1]

        # x 到达最下边，只能移动 y
        if x == len(nums) - 1:
            cache[x][y] = dfs(x, y + 1) + nums[x][y]
            return cache[x][y]
        # y 到达最右边，只能移动 x
        if y == len(nums[x]) - 1:
            cache[x][y] = dfs(x + 1, y) + nums[x][y]
            return cache[x][y]

        if cache[x][y] != -1:
            return cache[x][y]

        cache[x][y] = min(dfs(x + 1, y), dfs(x, y + 1)) + nums[x][y]
        return cache[x][y]

    # 从 (0, 0) 的位置开始遍历
    res = dfs(0, 0)
    print(cache)
    return res


print(min_path_sum_cache([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))


# 自顶向下，需要考虑下标越界的情况
def min_path_sum_dp(nums):
    dp = [[-1] * len(nums[0]) for _ in nums]
    dp[0][0] = nums[0][0]

    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if i == 0 and j == 0:
                continue
            if i == 0:
                dp[i][j] = dp[i][j - 1] + nums[i][j]
                continue
            if j == 0:
                dp[i][j] = dp[i - 1][j] + nums[i][j]
                continue
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + nums[i][j]
    return dp[-1][-1]


path_ = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(min_path_sum_dp(path_))


# https://leetcode-cn.com/problems/unique-paths/
# 回溯的方法，顺便能拿到路径
def unique_paths_dfs(m, n):
    path_count = 0
    path_list = list()

    def dfs(x, y, path):
        if x == m or y == n:
            return

        if x == m - 1 and y == n - 1:
            nonlocal path_count
            path_count += 1
            path_list.append(path.copy())
            return

        path.append((x, y))
        dfs(x + 1, y, path)
        path.pop()

        path.append((x, y))
        dfs(x, y + 1, path)
        path.pop()

    dfs(0, 0, [])
    for _path in path_list:
        path_str = ''
        for sub_path in _path:
            path_str += f'{sub_path} ==> '
        path_str = path_str + f'{(m - 1, n - 1)}'
        print(path_str)
    return path_count


print(unique_paths_dfs(3, 7))


def unique_paths_dp(m, n):
    dp = [[1] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if j == 0:
                dp[i][j] = dp[i - 1][j]
                continue
            if i == 0:
                dp[i][j] = dp[i][j - 1]
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


print(unique_paths_dp(3, 7))


# 这里涉及到滚动数组的概念
# 可以理解为每次求解一行的解，每一列的值只与前一行相关
# 下一列的值也只与前一行和前一列相关，而前一行的值已经暂存在数组中，所以只需要取前一列的值
def unique_paths_dp_(m, n):
    if n < m:
        n, m = m, n
    dp = [1] * m
    for i in range(1, n):
        for j in range(1, m):
            dp[j] += dp[j - 1]
    return dp[-1]


print(unique_paths_dp_(3, 7))


# https://leetcode-cn.com/problems/unique-paths-ii/
def unique_paths_dp_ii(matrix_):
    if not matrix_:
        return 0

    n, m = len(matrix_), len(matrix_[0])
    dp = [0] * m
    if matrix_[0][0] == 0:
        dp[0] = 1

    for i in range(n):
        for j in range(m):
            if matrix_[i][j] == 1:
                dp[j] = 0
                continue
            if j - 1 > 0 and matrix_[i][j] == 0:
                dp[j] += dp[j - 1]
    return dp[-1]


# https://leetcode-cn.com/problems/jump-game/
def can_jump(nums):
    farthest, size = 0, len(nums)
    for i in range(size):
        farthest = max(farthest, i + nums[i])
        if farthest >= size - 1:
            return True
        if farthest <= i:
            return False
    return farthest >= size - 1


# tail to head
def can_jump_dp(nums):
    # 从后往前依次判断，当前的 left + i 是否能
    left = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        left = i if i + left >= left else left
    return left == 0


print(can_jump([3, 2, 1, 0, 4]))


# https://leetcode-cn.com/problems/jump-game-ii/
def jump(nums):
    dp = [1] * len(nums)
    dp[0] = 0
    for i in range(1, len(nums)):
        temp_list = [dp[i - j] for j in range(nums[i]) if i - j >= 0]
        print(f'now temp_list is {temp_list}, now i is {i}')
        dp[i] = min(temp_list) + 1
    return dp[-1]


print(jump([2, 3, 1, 1, 4]))
