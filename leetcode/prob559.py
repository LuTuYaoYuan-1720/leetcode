# coding:utf-8


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    global l
    l = []

    def maxDepth(self, root: 'Node') -> int:
        global l
        self.dfs(root, 1)
        res = max(l)
        l = []
        return res

    def dfs(self, root: 'Node', depth: int):
        if len(root.children) == 0:
            global l
            l.append(depth)
            return

        for node in root.children:
            self.dfs(node, depth + 1)
