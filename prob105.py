# coding:utf-8
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder = preorder
        self.inorder = inorder

        self.index = {inorder[index]: index for index in range(len(inorder))}

        return self.f(0, len(preorder) - 1, 0, len(preorder) - 1)

    def f(self, preorder_left_index, preorder_right_index, inorder_left_index, inorder_right_index) -> TreeNode:
        if preorder_left_index > preorder_right_index:
            return None

        preorder_root_index = preorder_left_index
        inorder_root_index = self.index[self.preorder[preorder_root_index]]

        root = TreeNode(self.preorder[preorder_root_index])

        left_subtree_len = inorder_root_index - inorder_left_index

        root.left = self.f(preorder_left_index + 1, preorder_left_index + left_subtree_len, inorder_left_index,
                           inorder_root_index - 1)

        root.right = self.f(preorder_left_index + 1 + left_subtree_len, preorder_right_index, inorder_root_index + 1,
                            inorder_right_index)

        return root


s = Solution()
s.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
