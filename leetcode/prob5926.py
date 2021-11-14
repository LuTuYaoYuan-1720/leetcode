# coding:utf-8
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt = 0

        while tickets[k] != 1:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    cnt += 1

        for i in range(k):
            if tickets[i] != 0:
                cnt += 1

        return cnt + 1


s = Solution()
print(s.timeRequiredToBuy([84, 49, 5, 24, 70, 77, 87, 8], 3))
