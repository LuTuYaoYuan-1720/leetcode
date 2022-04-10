# coding:utf-8

class Solution:
    def minimizeResult(self, expression: str) -> str:
        lr = expression.split('+')
        l = lr[0]
        r = lr[1]
        nums = []
        allindex = []
        for i in range(len(l)):
            for j in range(len(r)):
                if i == 0 and j == len(r) - 1:
                    num = int(l[i:]) + int(r[:j + 1])
                elif i == 0:
                    num = (int(l[i:]) + int(r[:j + 1])) * int(r[j + 1:])
                elif j == len(r) - 1:
                    num = int(l[:i]) * (int(l[i:]) + int(r[:j + 1]))
                else:
                    num = int(l[:i]) * (int(l[i:]) + int(r[:j + 1])) * int(r[j + 1:])
                print(num)
                nums.append(num)
                allindex.append([i, j])
        mn = min(nums)
        index = allindex[nums.index(mn)]
        print(mn, index)
        res = l[:index[0]] + '(' + l[index[0]:] + '+' + r[:index[1] + 1] + ')' + r[index[1] + 1:]
        print(res)
        return res

s = Solution()
s.minimizeResult("247+38")
