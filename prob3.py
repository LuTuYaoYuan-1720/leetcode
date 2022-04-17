# coding:utf-8
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        cnt = {}
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
