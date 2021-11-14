"""
输入：rolls = [3,2,4,3], mean = 4, n = 2
输出：[6,6]
解释：所有 n + m 次投掷的平均值是 (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4 。
"""


class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        nsum = (n + len(rolls)) * mean - sum(rolls)
        if nsum < n or nsum > n * 6:
            return []
        else:
            return self.f(n, nsum)

    def f(self, n, nsum):
        res = []

        mean = nsum // n
        remain = nsum % n
        for i in range(n):
            res.append(mean)

        for i in range(remain):
            res[i] += 1
        return res


s = Solution()
print(s.missingRolls(rolls=[3, 2, 4, 3], mean=4, n=2))
print(s.missingRolls(rolls=[1, 5, 6], mean=3, n=4))
print(s.missingRolls(rolls=[1, 2, 3, 4], mean=6, n=4))
print(s.missingRolls(rolls=[1], mean=3, n=1))
