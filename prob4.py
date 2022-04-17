# coding:utf-8
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = [0] * (len(nums1) + len(nums2))
        i, i1, i2 = 0, 0, 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                nums[i] = nums1[i1]
                i1 += 1
                i += 1
            else:
                nums[i] = nums2[i2]
                i2 += 1
                i += 1

        while i1 < len(nums1):
            nums[i] = nums1[i1]
            i1 += 1
            i += 1
        while i2 < len(nums2):
            nums[i] = nums2[i2]
            i2 += 1
            i += 1

        if len(nums) % 2 == 1:
            return float(nums[len(nums) // 2])
        else:
            return float((nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2)
