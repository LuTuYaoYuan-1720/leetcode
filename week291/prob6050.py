# coding:utf-8
from collections import Counter


class Solution:
    def appealSum(self, s: str) -> int:
        ans, sum_g, pos = 0, 0, [-1] * 26
        for i, c in enumerate(s):
            c = ord(c) - ord('a')
            sum_g += i - pos[c]
            ans += sum_g
            print(sum_g)
            pos[c] = i
        return ans

        # res = 0
        # for i in range(1, len(s) + 1):
        #     res += i * (len(s) + 1 - i)
        #
        # cnt = {}
        # for i, c in enumerate(s):
        #     if c not in cnt:
        #         cnt[c] = [i]
        #     else:
        #         cnt[c].append(i)
        #
        # for idx_arr in cnt.values():
        #     for l in range(1, len(idx_arr)):
        #         for i in range(len(idx_arr) - l):
        #             pre, end = idx_arr[i], idx_arr[l + i]
        #             res -= (pre + 1) * (len(s) - end)
        #
        # return res

        # res = 0
        # for i in range(len(s)):
        #     cur_set = set()
        #     for j in range(i, len(s)):
        #         cur_set.add(s[j])
        #         res += len(cur_set)
        #
        # return res

        # res = 0
        #
        # for i in range(2, len(s) + 1):
        #     cnt = Counter(s[:i])
        #     res += len(cnt)
        #     for j in range(i, len(s)):
        #         cnt[s[j]] += 1
        #         cnt[s[j - i]] -= 1
        #         if cnt[s[j - i]] == 0:
        #             cnt.pop(s[j - i])
        #         res += len(cnt)
        #
        # return res + len(s)


s = Solution()
print(s.appealSum("abbcab"))
print(s.appealSum("code"))
