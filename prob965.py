# coding:utf-8
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.dfs(root, root.val)

    def dfs(self, root: TreeNode, parentVal: int):
        if root is None:
            return True
        if root.val != parentVal:
            return False
        return self.dfs(root.left, root.val) and self.dfs(root.right, root.val)

        # if root is None:
        #     return True
        # elif root.left is None and root.right is None:
        #     return root.val == parentVal
        #
        # l = self.dfs(root.left, root.val)
        # r = self.dfs(root.right, root.val)
        # return l and r and root.val == parentVal


test = TreeNode(4)
test.left = TreeNode(4)
test.left.right = TreeNode(4)

test.right = TreeNode(9)
test.right.left = TreeNode(4)
test.right.left.right = TreeNode(4)
s = Solution()
s.isUnivalTree(test)
