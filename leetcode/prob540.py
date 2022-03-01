# coding:utf-8
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2

        while l < r:
            if mid == 0 and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if mid == len(nums) - 1 and nums[mid] != nums[mid - 1]:
                return nums[mid]
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            if mid % 2 != 0:
                if nums[mid - 1] == nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid + 1] == nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            mid = (l + r) // 2

        return nums[mid]
