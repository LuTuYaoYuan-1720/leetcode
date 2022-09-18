# coding:utf-8
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [([0] * n) for i in range(m)]
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        nums.extend((m * n - len(nums)) * [-1])
        print(nums)
        self.idx = 0
        self.recursive(res, 0, len(res[0]) - 1, 0, len(res) - 1, nums)
        return res

    def recursive(self, res, x1, x2, y1, y2, nums):
        if x1 > x2 or y1 > y2:
            return

        if y1 == y2:
            for i in range(x1, x2 + 1):
                res[y1][i] = nums[self.idx]
                self.idx += 1
        elif x1 == x2:
            for j in range(y1, y2 + 1):
                res[j][x1] = nums[self.idx]
                self.idx += 1
        else:
            for i in range(x1, x2 + 1):
                res[y1][i] = nums[self.idx]
                self.idx += 1

            for j in range(y1 + 1, y2):
                res[j][x2] = nums[self.idx]
                self.idx += 1

            for i in range(x2, x1 - 1, -1):
                res[y2][i] = nums[self.idx]
                self.idx += 1

            for j in range(y2 - 1, y1, -1):
                res[j][x1] = nums[self.idx]
                self.idx += 1

            self.recursive(res, x1 + 1, x2 - 1, y1 + 1, y2 - 1, nums)
