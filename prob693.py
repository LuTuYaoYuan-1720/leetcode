# coding:utf-8

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        tmp = n % 2
        n //= 2
        while n != 0:
            cur = n % 2
            if tmp == cur:
                return False
            tmp = cur % 2
            n //= 2

        return True


s = Solution()
s.hasAlternatingBits(7)
