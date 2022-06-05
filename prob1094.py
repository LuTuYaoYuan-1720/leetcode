# coding:utf-8
from typing import List
import queue
import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0 for i in range(1002)]
        for trip in trips:
            i = trip[1]
            j = trip[2] - 1
            val = trip[0]
            diff[i] += val
            if j + 1 < len(diff):
                diff[j + 1] -= val

        if diff[0] > capacity:
            return False

        for i in range(1, len(diff)):
            diff[i] += diff[i - 1]
            if diff[i] > capacity:
                return False

        return True


s = Solution()
s.carPooling([[9, 0, 1], [3, 3, 7]], 4)
s.carPooling([[2, 1, 5], [3, 5, 7]], 3)


queue.PriorityQueue()
heapq.heapify()