# coding:utf-8
class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        keyindex = []

        for i in range(len(nums)):
            if nums[i] == key:
                keyindex.append(i)
        res = set()

        for index in keyindex:
            for i in range(index - k, index + k + 1):
                if 0 <= i < len(nums):
                    res.add(i)

        return sorted(list(res))
