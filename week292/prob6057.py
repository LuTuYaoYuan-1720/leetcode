# coding:utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        self.dfs(root)
        return self.cnt

    def dfs(self, root: TreeNode):
        if root is None:
            return 0, 0

        lsum, lnum = self.dfs(root.left)
        rsum, rnum = self.dfs(root.right)
        if (lsum + rsum + root.val) // (lnum + rnum + 1) == root.val:
            self.cnt += 1
        return lsum + rsum + root.val, lnum + rnum + 1
