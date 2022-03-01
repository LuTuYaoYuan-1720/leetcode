# coding:utf-8
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        n = 503968
        res = 0
        num = 0
        for i in range(1, n + 1):
            neededApples -= num
            num = 8 * (i + 1) * (i + i + i) // 2 - 4 * i - 4 * 2 * i
            if neededApples - num <= 0:
                res = i
                break

        return res * 4 * 2


i = 3
num = 8 * (i + 1) * (i + i + i) // 2 - 4 * i - 4 * 2 * i
print(num)
