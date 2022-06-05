# coding:utf-8

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
删除倒数第 N 个   得先找到倒数第 N + 1 个
fast先行 N + 1 步   然后和slow一起走  当fast到达 null时
slow就刚好到倒数 N + 1
"""


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy
        for i in range(n + 1):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
