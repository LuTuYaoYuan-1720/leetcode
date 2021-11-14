from math import sqrt


class Solution:
    def arrangeCoins(self, n: int) -> int:
        pre = int(sqrt(n * 2)) - 1
        for i in range(5):
            num = (pre + i) * (pre + i + 1) / 2
            if num - n == 0:
                return pre + i
            elif 0 < num - n < pre + i:
                return pre + i - 1


s = Solution()
print(s.arrangeCoins(1))
print(s.arrangeCoins(8))
print(s.arrangeCoins(4))
print(s.arrangeCoins(10))
