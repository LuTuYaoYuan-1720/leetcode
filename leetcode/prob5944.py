# coding:utf-8
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        res = ''
        p = self.getParent(root, startValue, destValue)

        # print(self.DFS(p, startValue, ''))
        self.DFS(p, destValue, '')
        return res

    def getParent(self, root, node1, node2):

        if root is None or node1 is None or node2 is None:
            return None
        # 这里可以换成if(root == node1 || root == node2),我只是为了方便测试才这样写
        if root.val == node1 or root.val == node2:
            return root
        left = self.getParent(root.left, node1, node2)
        right = self.getParent(root.right, node1, node2)
        # 如果左右子树都能找到，那么当前节点就是最近的公共祖先节点
        if left is not None and right is not None:
            return root
        # 如果左子树上没有，那么返回右子树的查找结果
        if left is None:
            return right
        # 否则返回左子树的查找结果
        else:
            return left

    def DFS(self, root, destValue, path):
        if root is not None:
            print(root.val)

        if root.left is not None:
            self.DFS(root.left, destValue, path + 'L')
        if root.right is not None:
            self.DFS(root.right, destValue, path + 'R')
