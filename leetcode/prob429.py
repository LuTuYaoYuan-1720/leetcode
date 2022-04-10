# coding:utf-8


# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        res = [[root.val]]
        tmpNode = [root]
        while len(tmpNode) != 0:
            cur = []
            v = []
            for node in tmpNode:
                for child in node.children:
                    if child is not None:
                        cur.append(child)
                        v.append(child.val)
            res.append(v)
            tmpNode = cur

        return res[:-1]
