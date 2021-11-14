class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        for i in nums:
            max |= i

        all = self.getArraySubSet(nums)

        count = 0
        for l in all:
            if len(l) >= 1:
                ornum = 0
                for num in l:
                    ornum |= num
                if ornum == max:
                    count += 1

        return count

    def getArraySubSet(self, originArray):
        """
        :type originArray:list
        :rtype :listlist
        """
        result = [[]]
        size = len(originArray)
        for i in range(size):
            for j in range(len(result)):
                # 现有每个子集中添加新元素，作为新子集加入结果集中
                result.append(result[j] + [originArray[i]])
            # print(result)
        return result
