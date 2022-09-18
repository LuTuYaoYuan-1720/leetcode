# coding:utf-8

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []
        layer = [root]
        res.append(root.val)

        while len(layer) != 0:
            nextLayer = []
            nextLayerVal = []
            for node in layer:
                if node.left:
                    nextLayer.append(node.left)
                    nextLayerVal.append(node.left.val)
                if node.right:
                    nextLayer.append(node.right)
                    nextLayerVal.append(node.right.val)

            if len(nextLayer) == 0:
                break
            layer = nextLayer
            res.append(max(nextLayerVal))

        return res
