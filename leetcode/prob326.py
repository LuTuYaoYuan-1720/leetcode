# coding:utf-8

class Solution(object):
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        list = [1, 3]
        tmp = 3
        while tmp < n:
            tmp *= 3
            list.append(tmp)
        if n in list:
            return True
        else:
            return False


s = Solution()
print(s.isPowerOfThree(45))
