# coding:utf-8
from typing import List, Optional
from heapq import *
from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


"""python直接传不了比较器就巨傻逼"""


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        pq = PriorityQueue()
        for head in lists:
            pq.put(head)

        while not pq.empty():
            mn = pq.get()
            p.next = mn
            if mn.next is not None:
                pq.put(mn.next)
            p = p.next

        return dummy.next

        # res = ListNode()
        # heap = []
        # for l in lists:
        #     head = l
        #     while head is not None:
        #         heappush(heap, head.val)
        #         head = head.next
        #
        # p = res
        # while len(heap) != 0:
        #     p.next = ListNode(heappop(heap))
        #     p = p.next
        #
        # return res.next


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l3 = ListNode(2)
l3.next = ListNode(6)
lists = [l1, l2, l3]
s = Solution()
res = s.mergeKLists(lists)

while res is not None:
    print(res.val)
    res = res.next
