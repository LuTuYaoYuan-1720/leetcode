# coding:utf-8
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt = 0
        prod = 1
        i = 0
        for j, num in enumerate(nums):
            prod *= num
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
            cnt += j - i + 1
        return cnt

        # cnt = 0
        # for i in range(len(nums)):
        #     cur = nums[i]
        #     if cur < k:
        #         cnt += 1
        #     for j in range(i + 1, len(nums)):
        #         cur *= nums[j]
        #         if cur < k:
        #             cnt += 1
        #         else:
        #             break
        # return cnt


s = Solution()
s.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
