# coding:utf-8
class Solution:
    def minimumLength(self, s: str) -> int:
        res = list(s)

        while len(res) > 1:
            pre = res[0]
            back = res[len(res) - 1]

            if pre == back:
                lindex = 0
                rindex = len(res) - 1

                while lindex + 1 < rindex:
                    if res[lindex + 1] == pre:
                        lindex += 1
                    else:
                        break
                while rindex - 1 > lindex:
                    if res[rindex - 1] == back:
                        rindex -= 1
                    else:
                        break
                res = res[0:rindex]
                res = res[lindex + 1:]
            else:
                break

        return len(res)


s = Solution()
print(s.minimumLength("abca"))
print(s.minimumLength("cabaabac"))
print(s.minimumLength("ca"))
print(s.minimumLength("aabccabba"))
