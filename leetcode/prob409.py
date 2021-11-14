# coding:utf-8
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for i in range(0, len(nums1)):
            minNumArr = [num for num in nums2[nums2.index(nums1[i]) + 1: len(nums2)] if num > nums1[i]]

            if len(minNumArr) > 0:
                res.append(minNumArr[0])
            else:
                res.append(-1)

        return res


s = Solution()
print(s.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(s.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))
