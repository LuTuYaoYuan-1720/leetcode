# coding:utf-8

class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0

        for i in range(1, len(directions)):
            if directions[i - 1] == 'L' and directions[i] == 'R':
                i += 1
            elif directions[i - 1] == directions[i]:
                i += 1
            elif directions[i - 1] == 'R' and directions[i] == 'L':
                directions = directions[:i - 1] + 'SS' + directions[i + 1:]
                res += 2
                i += 1
            else:
                directions = directions[:i - 1] + 'SS' + directions[i + 1:]
                res += 1
                i += 1
        return res


s = Solution()
s.countCollisions(directions="LLSRSSRSSLLSLLLRSLSRL")
