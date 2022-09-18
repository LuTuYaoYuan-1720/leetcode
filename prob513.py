# coding:utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # 记录当前层
        layer = [root]

        while len(layer) != 0:
            # 记录当前层的下一层
            nextLayer = []
            for node in layer:
                if node.left is not None:
                    nextLayer.append(node.left)
                if node.right is not None:
                    nextLayer.append(node.right)
            if len(nextLayer) == 0:
                break
            layer = nextLayer

        return layer[0].val
