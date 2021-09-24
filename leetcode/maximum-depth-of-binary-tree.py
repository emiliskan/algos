"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left_path = 0
        right_path = 0

        left_path += self.max_depth(root.left)
        right_path += self.max_depth(root.right)

        return max(left_path, right_path) + 1

