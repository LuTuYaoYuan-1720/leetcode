# coding:utf-8
from typing import List, Optional
from heapq import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        heap = []
        for l in lists:
            head = l
            while head is not None:
                heappush(heap, head.val)
                head = head.next

        p = res
        while len(heap) != 0:
            p.next = ListNode(heappop(heap))
            p = p.next

        return res.next
