# coding:utf-8
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if ord(target) >= ord(letters[-1]):
            return letters[0]

        l, r = 0, len(letters) - 1
        while l < r:
            mid = (l + r) // 2
            if ord(target) >= ord(letters[mid]):
                l = mid + 1
            else:
                r = mid
        return letters[l]


s = Solution()
print(s.nextGreatestLetter(letters=["c", "d", "d", "d", "f", "j"], target="d"))
