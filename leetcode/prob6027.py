# coding:utf-8
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        feng = []
        gu = []
        for i in range(1, len(nums) - 1):
            left = i - 1
            while left > 0:
                if nums[left] != nums[i]:
                    break
                left -= 1

            right = i + 1
            while right < len(nums) - 1:
                if nums[right] != nums[i]:
                    break
                right += 1

            if nums[left] > nums[i] and nums[right] > nums[i]:
                feng.append(i)
            if nums[left] < nums[i] and nums[right] < nums[i]:
                gu.append(i)
        res = len(feng) + len(gu)
        for i in range(len(feng) - 1):
            if feng[i + 1] - feng[i] == 1:
                res -= 1

        for i in range(len(gu) - 1):
            if gu[i + 1] - gu[i] == 1:
                res -= 1
        return res


s = Solution()
s.countHillValley(
    [57, 57, 57, 57, 57, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 85, 85, 85, 86, 86, 86])
s.countHillValley([2, 4, 1, 1, 6, 5])
s.countHillValley([6, 5, 10])
