# coding:utf-8
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = nums1[:m]
        i1 = 0
        i2 = 0
        index = 0
        while i1 < m and i2 < n:
            if tmp[i1] < nums2[i2]:
                nums1[index] = tmp[i1]
                index += 1
                i1 += 1
            else:
                nums1[index] = nums2[i2]
                index += 1
                i2 += 1

        if i1 < m:
            for i in range(i1, m):
                nums1[index] = tmp[i]
                index += 1

        if i2 < n:
            for i in range(i2, n):
                nums1[index] = nums2[i]
                index += 1
