# coding:utf-8

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # 有 c 就判断前面有没有 ab
        for c in s:
            if len(stack) >= 2 and c == 'c' and stack[-1] == 'b' and stack[-2] == 'a':
                stack.pop()
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0


s = Solution()
s.isValid("abacbcabcc")
