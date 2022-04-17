# coding:utf-8
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empty = numBottles
        res += numBottles
        while empty >= numExchange:
            numBottles = empty // numExchange
            empty = numBottles + empty % numExchange
            res += numBottles

        return res

s = Solution()
print(s.numWaterBottles(numBottles=9, numExchange=3))
