# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []

        self.recur(root, l)
        res = l[k - 1]
        return res

    def recur(self, root, l: list):
        if root.left is not None:
            self.recur(root.left, l)

        l.append(root.val)

        if root.right is not None:
            self.recur(root.right, l)
