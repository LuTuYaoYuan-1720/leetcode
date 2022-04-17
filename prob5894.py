class Solution(object):
    def twoOutOfThree(self, nums1: list, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        num = set()
        for i in nums1:
            num.add(i)
        for i in nums2:
            num.add(i)
        for i in nums3:
            num.add(i)

        res = []
        for item in num:
            count = 0
            if item in nums1:
                count += 1
            if item in nums2:
                count += 1
            if item in nums3:
                count += 1
            if count >= 2:
                res.append(item)

        return res


s = Solution()
print(s.twoOutOfThree(nums1=[1, 1, 3, 2], nums2=[2, 3], nums3=[3]))
print(s.twoOutOfThree(nums1=[3, 1], nums2=[2, 3], nums3=[1, 2]))
print(s.twoOutOfThree(nums1=[1, 2, 2], nums2=[4, 3, 3], nums3=[5]))
