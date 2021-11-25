# coding:utf-8
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1 = []
        l2 = []
        self.help(root1, l1)
        self.help(root2, l2)
        return l1 == l2

    def help(self, root: TreeNode, record: List):
        if root.left is not None:
            self.help(root.left, record)

        if root.left is None and root.right is None:
            record.append(root.val)

        if root.right is not None:
            self.help(root.right, record)
