# coding:utf-8
import bisect
from typing import List


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def cal(arr):
            brr = []
            for a in arr:
                if brr == [] or a >= brr[-1]:
                    brr.append(a)
                else:
                    idx = bisect.bisect(brr, a)
                    brr[idx] = a
            return len(arr) - len(brr)

        res = 0
        for i in range(k):
            brr = []
            cur = i
            while cur < len(arr):
                brr.append(arr[cur])
                cur += k
            res += cal(brr)
        return res


s = Solution()
s.kIncreasing(arr=[4, 1, 5, 2, 6, 2], k=3)
print(s.kIncreasing([12, 6, 12, 6, 14, 2, 13, 17, 3, 8, 11, 7, 4, 11, 18, 8, 8, 3], 1))
