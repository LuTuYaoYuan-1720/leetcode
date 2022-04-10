# coding:utf-8
from typing import List


# 获取每一层的最后一个即可
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        res = []
        cnt = [[root]]
        cur = []
        if root.left is not None:
            cur.append(root.left)
        if root.right is not None:
            cur.append(root.right)
        cnt.append(cur)
        while len(cur) != 0:

            tmp = []
            for leaf in cur:
                if leaf.left is not None:
                    tmp.append(leaf.left)
                if leaf.right is not None:
                    tmp.append(leaf.right)
            cnt.append(tmp)
            cur = tmp

        for i in range(len(cnt) - 1):
            res.append(cnt[i][-1].val)

        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
s = Solution()
s.rightSideView(root)
