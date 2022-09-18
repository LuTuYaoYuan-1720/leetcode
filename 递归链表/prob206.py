# coding:utf-8

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # # 递归
    # def reverseList(self, head: ListNode) -> ListNode:
    #     if head.next is None or head is None:
    #         return head
    #     last = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return last

    # 迭代
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        cur = head.next
        head.next = None
        while cur is not None:
            nxt = cur.next
            cur.next = head
            head = cur

            cur = nxt

        return head
