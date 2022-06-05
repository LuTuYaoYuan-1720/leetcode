# coding:utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
一边 先遍历完A 再遍历B
另一边 先遍历完B 再遍历A
如果有相交  在第二部分就会有重叠
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB
        lenA = lenB = 0
        while p1 is not None:
            lenA += 1
            p1 = p1.next
        while p2 is not None:
            lenB += 1
            p2 = p2.next

        p1, p2 = headA, headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                p1 = p1.next
        else:
            for i in range(lenB - lenA):
                p2 = p2.next

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1

        # p1 = headA
        # p2 = headB
        #
        # while p1 != p2:
        #     if p1 is not None:
        #         p1 = p1.next
        #     else:
        #         p1 = headB
        #     if p2 is not None:
        #         p2 = p2.next
        #     else:
        #         p2 = headA
        #
        # return p1
