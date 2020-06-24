"""
LeetCode 210 课程表
https://blog.csdn.net/fuxuemingzhu/article/details/83302328
"""
from typing import List
import collections


# BFS
# 拓扑排序  依次找到入度为 0 的节点，并将该节点指向的节点，将其节点的入度 -1
class Solution(object):
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 图邻接列表，字典的表示方法
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1
        path = []
        for i in range(numCourses):
            zeroDegree = False
            for j in range(numCourses):
                if indegrees[j] == 0:
                    zeroDegree = True
                    break
            if not zeroDegree:
                return []
            indegrees[j] -= 1
            path.append(j)
            for node in graph[j]:
                indegrees[node] -= 1
        return path


res = Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
print(res)
