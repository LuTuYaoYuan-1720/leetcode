# coding:utf-8

# 头插法
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        start = ListNode()
        start.next = head

        cur = head.next
        head.next = None
        while cur is not None:
            tmp = cur.next

            cur.next = start.next
            start.next = cur
            cur = tmp

        return start.next


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
s = Solution()
s.reverseList(l)
