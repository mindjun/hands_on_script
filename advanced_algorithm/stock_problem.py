"""
股票问题
https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/tuan-mie-gu-piao-wen-ti
定义状态：
    dp[i][k][0 or 1]
    0 <= i <= n-1, 1 <= k <= K
    n 为天数，大 K 为最多交易数
    此问题共 n × K × 2 种状态，全部穷举就能搞定。

    # 用以下方式进行穷举
    for 0 <= i < n:
        for 1 <= k <= K:
            for s in {0, 1}:
                dp[i][k][s] = max(buy, sell, rest)

    base case：
    dp[-1][k][0] = 0
    解释：因为 i 是从 0 开始的，所以 i = -1 意味着还没有开始，这时候的利润当然是 0 。
    dp[-1][k][1] = -infinity
    解释：还没开始的时候，是不可能持有股票的，用负无穷表示这种不可能。
    dp[i][0][0] = 0
    解释：因为 k 是从 1 开始的，所以 k = 0 意味着根本不允许交易，这时候利润当然是 0 。
    dp[i][0][1] = -infinity
    解释：不允许交易的情况下，是不可能持有股票的，用负无穷表示这种不可能。

    状态转移方程：
    没有持有，前一天没有持有，前一天持有然后卖掉
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
    持有，前一天持有，前一天没有持有买入
    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

==>
    base case：
    dp[-1][k][0] = dp[i][0][0] = 0
    dp[-1][k][1] = dp[i][0][1] = -infinity

    状态转移方程：
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
"""
from typing import List


# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
def max_profit_1(prices):
    if not prices:
        return 0
    # dp = [[0, 1]] * len(prices)
    dp_i_0, dp_i_1 = 0, float('-inf')
    for i in range(len(prices)):
        # if i == 0:
        #     第一天未持有，为 0
        #     dp[i][0] = 0
        #     第一天持有，为 -prices[i]
        #     dp[i][1] = -prices[i]
        #     continue
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # 因为只允许买卖一次，所以为 -prices[i]
        dp_i_1 = max(dp_i_1, -prices[i])
        # dp[i][1] = max(dp[i-1][1], -prices[i])
    # return dp[-1][0]
    return dp_i_0


# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
# 允许买卖无限次和允许买卖一次的状态转移相似，只需要将 k 去掉
def max_profit_2(prices: List[int]) -> int:
    dp_i_0, dp_i_1 = 0, float('-inf')
    # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    for i in range(len(prices)):
        temp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, temp - prices[i])
    return dp_i_0


# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/
# 需要在卖出之后才能买入
def max_profit_3(prices: List[int]) -> int:
    # # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    # # dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    # # 解释：第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。
    #
    # dp_i_0, dp_i_1 = 0, float('-inf')
    # # 代表 dp[i-2][0]
    # dp_pre_0 = 0
    # for i in range(len(prices)):
    #     temp = dp_i_0
    #
    #     dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
    #     dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
    #     dp_pre_0 = temp
    # return dp_i_0

    if len(prices) <= 1:
        return 0
    max_k = 2
    dp = [[[0, 0] for _ in range(max_k + 1)] for _ in range(len(prices))]
    dp[0][2][0] = 0  # 第0天，不管还剩几次交易次数，不持有收益是0，也不可能持有(一天内不能瞬间买入卖出)，所以设1为负数
    dp[0][2][1] = -prices[0]
    dp[0][1][0] = 0
    dp[0][1][1] = -prices[0]

    for i in range(1, len(prices)):
        # k正着还是倒着，就看前面桌面定义的，
        # 1、正着定义base case时，k代表已交易次数，从0开始，0，1
        # 2、倒着定义base case时，k代表剩余交易次数，从2开始，2，1
        for k in range(max_k, 0, -1):  # 这里必须倒着，base case中k是倒着的，这里正序会出现0，1，与前面的设定不同了，就会出错
            dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
            dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
    return dp[-1][max_k][0]


print(max_profit_3([2, 1, 2, 0, 1]))
