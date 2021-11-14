"""
输入：S = "2-5g-3-J", K = 2
输出："2-5G-3J"

输入：S = "5F3Z-2e-9-w", K = 4
输出："5F3Z-2E9W"
"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        l = list(s.upper()[::])
        while '-' in l:
            l.remove('-')
        res = ''
        l.reverse()
        count = 0
        for i in l:
            res += i
            count += 1
            if count % k == 0 and count != len(l):
                res += '-'
        return res[::-1]


s = Solution()
print(s.licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(s.licenseKeyFormatting("2-5g-3-J", 2))
