# coding:utf-8

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        help = ListNode()
        help.next = head
        startPre = self.f(help, left - 1)
        end = self.f(startPre, right - left + 1)
        last = end.next
        end.next = None
        start = startPre.next
        startPre.next = None
        re = self.rever(start)
        tmp = re
        for i in range(right - left):
            tmp = tmp.next
        tmp.next = last
        startPre.next = re

        return head

    def rever(self, head: ListNode) -> ListNode:
        res = ListNode()
        res.next = head
        cur = head.next
        while cur is not None:
            head.next = cur.next
            cur.next = res.next
            res.next = cur
            cur = head.next

        return res.next

    def f(self, head: ListNode, nums: int) -> ListNode:
        res = head
        for i in range(nums):
            res = res.next
        return res
