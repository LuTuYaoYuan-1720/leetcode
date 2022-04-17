# coding:utf-8

class Solution:
    def isValid(self, s: str) -> bool:
        sign = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and sign.get(s[i]) == stack[-2]:
                stack.pop()
                stack.pop()
        if len(stack) == 0:
            return True
        return False
