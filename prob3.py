# coding:utf-8
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        cnt = {}
        # 也是滑动窗口那么个意思， 一旦窗口内有一个字符出现两次， 就要缩小窗口至其保持所有都出现一次
        for r in range(0, len(s)):
            if s[r] not in cnt.keys():
                cnt[s[r]] = 1
            else:
                res = max(res, r - l)
                l = s[:r].rfind(s[r]) + 1
                cnt = Counter(s[l:r + 1])

        return max(res, len(cnt))


s = Solution()
print(s.lengthOfLongestSubstring(s="dvdf"))
print(s.lengthOfLongestSubstring(s="abcabcbb"))
