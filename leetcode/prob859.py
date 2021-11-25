# coding:utf-8
from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        cnt = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                cnt.append(i)

        if len(cnt) == 2 and s[cnt[0]] == goal[cnt[1]] and s[cnt[1]] == goal[cnt[0]]:
            return True
        elif len(cnt) < 2:
            c = Counter(s)
            for v in c.values():
                if v >= 2:
                    return True

        return False


s = Solution()
print(s.buddyStrings(s="ab", goal="ba"))
print(s.buddyStrings(s="ab", goal="ab"))
print(s.buddyStrings(s="aa", goal="aa"))
print(s.buddyStrings(s="aaaaaaabc", goal="aaaaaaacb"))
