# coding:utf-8

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        slow, fast = head, head
        while fast is not None:
            if slow.val != fast.val:
                slow = slow.next
                slow.val = fast.val
            fast = fast.next

        slow.next = None

        return head
