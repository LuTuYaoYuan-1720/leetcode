# coding:utf-8
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s = ''
        while head is not None:
            s += str(head.val)
            head = head.next

        return s == s[::-1]
