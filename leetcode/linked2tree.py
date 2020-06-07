"""
leetcode 109
"""
import math
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


temp_list = list(range(7))


def get_tree(nums: List):
    if len(nums) == 1:
        return TreeNode(nums[0])
    if len(nums) == 0:
        return None

    mid = math.floor(len(nums)/2)
    root = TreeNode(nums[mid])
    root.left = get_tree(nums[:mid])
    root.right = get_tree(nums[mid+1:])

    return root


res = get_tree(temp_list)
print(res)
