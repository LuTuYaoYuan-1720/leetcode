# coding:utf-8

class Solution:
    """
    如果有对应的左括号和右括号相匹配，就不用计数，单独的右括号得有一个左括号
    最后栈里的都是左括号
    """

    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        stack = []

        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    res += 1

        return res + len(stack)
