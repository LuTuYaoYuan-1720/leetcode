# coding:utf-8
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        l = 0
        r = len(nums) - 1

        while l < r:
            for i in range(l, r + 1):
                if nums[i] % 2 != 0:
                    l = i
                    break
            for i in range(r, l, -1):
                if nums[i] % 2 == 0:
                    r = i
                    break
            if l < r:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp

            l += 1
            r -= 1

        return nums

s = Solution()
print(s.sortArrayByParity([0, 1]))
