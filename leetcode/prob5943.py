# coding:utf-8

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_len = 0
        p = head
        while p is not None:
            list_len += 1
            p = p.next

        p = head
        for i in range(list_len // 2 - 1):
            p = p.next

        if p.next is not None:
            p.next = p.next.next
        else:
            p.next = None

        return head
