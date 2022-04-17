# coding:utf-8
class Solution:
    def countPoints(self, rings: str) -> int:
        res = 0

        cnt = [[0 for col in range(3)] for row in range(10)]

        for i in range(len(rings) // 2):
            tmp = rings[2 * i: 2 * i + 2]
            if tmp[0] == 'R':
                cnt[int(tmp[1])][0] += 1
            if tmp[0] == 'G':
                cnt[int(tmp[1])][1] += 1
            if tmp[0] == 'B':
                cnt[int(tmp[1])][2] += 1

        for i in range(10):
            if cnt[i][0] > 0 and cnt[i][1] > 0 and cnt[i][2] > 0:
                res += 1

        return res


s = Solution()
print(s.countPoints("B0B6G0R6R0R6G9"))
