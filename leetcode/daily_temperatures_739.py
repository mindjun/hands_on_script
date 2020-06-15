"""
leetcode 739
主要思想是单调递增栈，用列表来实现
"""
from leetcode import *


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0 for _ in range(len(T))]
        stack = list()

        for i in range(len(T))[::-1]:
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            res[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# [1, 1, 4, 2, 1, 1, 0, 0]
print(Solution().dailyTemperatures(temperatures))
