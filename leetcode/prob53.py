# coding:utf-8
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        pre = 0
        for i in range(len(nums)):
            pre = max(pre + nums[i], nums[i])
            res = max(pre, res)
        return res


s = Solution()
print(s.maxSubArray([5, 4, -1, 7, 8]))
