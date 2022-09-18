# coding:utf-8

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left, right = 0, 0
        window = {}
        while right < len(s):
            cur = s[right]
            right += 1
            if cur in window:
                window[cur] += 1
            else:
                window[cur] = 1

            # 当窗口扩大至有一个字符出现两次， 就要缩小窗口至其保持所有字符只出现一次
            while window[cur] > 1:
                d = s[left]
                left += 1
                window[d] -= 1

            res = max(res, right - left)

        return res


s = Solution()
s.lengthOfLongestSubstring("pwwkew")
