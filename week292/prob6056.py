# coding:utf-8

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        mx = -1
        for i in range(len(num) - 2):
            cur = num[i:i + 3]
            if cur[0] == cur[1] == cur[2]:
                mx = max(mx, int(cur))

        if mx == -1:
            return ''
        elif mx == 0:
            return '000'
        else:
            return str(mx)
