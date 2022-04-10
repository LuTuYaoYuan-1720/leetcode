# coding:utf-8

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.res = ''
        self.dfs(root)
        return self.res[1:-1]

    def dfs(self, root: TreeNode):
        self.res += '('
        self.res += str(root.val)

        # 左边为空右边不为空就得加 ()
        if root.left is not None:
            self.dfs(root.left)
        elif root.right is not None:
            self.res += '()'

        if root.right is not None:
            self.dfs(root.right)

        self.res += ')'
