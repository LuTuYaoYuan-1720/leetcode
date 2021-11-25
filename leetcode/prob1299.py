# coding:utf-8
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        res = [-1]
        m = arr[len(arr) - 1]
        for i in range(len(arr) - 2, -1, -1):
            res.append(m)
            if arr[i] > m:
                m = arr[i]

        return res[::-1]


s = Solution()
print(s.replaceElements(arr=[17, 18, 5, 4, 6, 1]))
