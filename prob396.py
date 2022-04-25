# coding:utf-8
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        all = []
        start = 0
        for i, num in enumerate(nums):
            start += i * num
        all.append(start)

        subsum = []
        nums.extend(nums[:-1])
        pre = sum(nums[:n - 1])
        for i in range(n - 1):
            cur = pre - nums[i] + nums[i + n - 1]
            subsum.append(cur)
            pre = cur

        for i in range(n - 1):
            all.append(all[-1] - subsum[i] + nums[i] * (n - 1))

        return max(all)


s = Solution()
print(s.maxRotateFunction(nums=[4, 3, 2, 6]))
