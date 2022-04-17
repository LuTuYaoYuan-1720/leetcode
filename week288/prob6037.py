# coding:utf-8
class Solution:
    def largestInteger(self, num: int) -> int:
        res = ''
        num = str(num)
        ji = []
        jiindex = []
        ou = []
        ouindex = []
        for i in range(len(num)):
            if int(num[i]) % 2 == 0:
                ou.append(int(num[i]))
                ouindex.append(i)
            else:
                ji.append(int(num[i]))
                jiindex.append(i)
        ji = sorted(ji, reverse=True)
        ou = sorted(ou, reverse=True)
        o, j = 0, 0
        for i in range(len(num)):
            if o < len(ouindex) and i == ouindex[o]:
                res += str(ou[o])
                o += 1
            if j < len(jiindex) and i == jiindex[j]:
                res += str(ji[j])
                j += 1

        return int(res)
