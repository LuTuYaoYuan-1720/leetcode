# coding:utf-8

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指针
        fast = head
        slow = head

        while slow is not None and fast is not None:
            slow = slow.next
            if fast.next is not None:
                fast = fast.next.next
            else:
                return False
            if slow == fast:
                return True

        return False


head = ListNode(1)
head.next = ListNode(2)
s = Solution()
s.hasCycle(head)
