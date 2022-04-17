# coding:utf-8
class Solution:
    def bulbSwitch(self, n: int) -> int:
        cnt = n
        sign = [1] * (n + 1)

        for i in range(2, n + 1):
            j = 1
            while i * j <= n:
                if sign[i * j] == 1:
                    sign[i * j] = 0
                    cnt -= 1
                else:
                    sign[i * j] = 1
                    cnt += 1
                j += 1

        return cnt


s = Solution()
print(s.bulbSwitch(3))
