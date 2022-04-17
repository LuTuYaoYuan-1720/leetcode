# coding:utf-8
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        start = 0
        end = 0

        while end < len(nums) - 1:
            if nums[end + 1] - nums[end] == 1:
                end += 1
            else:
                if start != end:
                    res.append(f'{nums[start]}->{nums[end]}')
                else:
                    res.append(str(nums[end]))
                start = end + 1
                end = start

        if start != end:
            res.append(f'{nums[start]}->{nums[end]}')
        else:
            res.append(str(nums[end]))

        return res


s = Solution()
print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
print(s.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
