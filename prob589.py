from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.res = []
        self.DFS(root)
        return self.res

    def DFS(self, root: 'Node'):
        if root is None:
            return

        self.res.append(root.val)

        for children in root.children:
            self.DFS(children)
