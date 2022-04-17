# coding:utf-8
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        p = res
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                cur = ListNode(list2.val)
                p.next = cur
                p = p.next
                list2 = list2.next
            else:
                cur = ListNode(list1.val)
                p.next = cur
                p = p.next
                list1 = list1.next

        if list1 is not None:
            p.next = list1
        if list2 is not None:
            p.next = list2

        return res.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
s = Solution()
