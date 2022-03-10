# coding:utf-8
from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        res = 0
        nums = sorted(nums)
        count = 0

        if nums[0] > 1:
            if nums[0] - 1 <= k:
                res += (1 + nums[0] - 1) * (nums[0] - 1) // 2
                count += nums[0] - 1
            else:
                res += (1 + k) * k // 2
                count += k

        for i in range(len(nums) - 1):
            if count == k:
                break
            n1 = nums[i]
            n2 = nums[i + 1]
            if n1 == n2:
                continue
            if n2 - (n1 + 1) <= k - count:
                res += (n1 + 1 + n2 - 1) * (n2 - (n1 + 1)) // 2
                count += n2 - (n1 + 1)
            else:
                res += (n1 + 1 + n1 + k - count) * (k - count) // 2
                count += k - count

        res += (nums[-1] + 1 + nums[-1] + k - count) * (k - count) // 2

        return res


s = Solution()
print(s.minimalKSum(
    [96, 44, 99, 25, 61, 84, 88, 18, 19, 33, 60, 86, 52, 19, 32, 47, 35, 50, 94, 17, 29, 98, 22, 21, 72, 100, 40, 84],
    35))
