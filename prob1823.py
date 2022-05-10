# coding:utf-8
from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque(range(1, n + 1))
        while len(q) > 1:
            for _ in range(k - 1):
                q.append(q.popleft())
            q.popleft()
        return q[0]

        # sign = [0] * n
        # idx = -1
        # delper = []
        # while len(delper) < n - 1:
        #     cnt = 0
        #     while cnt < k:
        #         idx = (idx + 1) % n
        #         if sign[idx] != 1:
        #             cnt += 1
        #     sign[idx] = 1
        #     delper.append(idx + 1)
        #
        # delper.sort()
        # for i, num in enumerate(delper):
        #     if i != num - 1:
        #         return i + 1
        # return n


s = Solution()
s.findTheWinner(3, 1)
