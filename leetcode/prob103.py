# coding:utf-8
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        res = []

        tmp = [root]
        cur = []
        floor = 1
        while len(tmp) != 0:
            if floor % 2 == 0:
                res.append([leaf.val for leaf in tmp][::-1])
            else:
                res.append([leaf.val for leaf in tmp])
            floor += 1

            for leaf in tmp:
                if leaf.left is not None:
                    cur.append(leaf.left)
                if leaf.right is not None:
                    cur.append(leaf.right)

            tmp = cur
            cur = []

        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
s.zigzagLevelOrder(root)

l = [1, 2, 3]
print(list(reversed(l)))
