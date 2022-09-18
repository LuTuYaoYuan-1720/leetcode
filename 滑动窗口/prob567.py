# coding:utf-8
from collections import Counter


class Solution:
    def checkInclusion(self, target: str, s: str) -> bool:
        need, window = Counter(target), {}
        left, right = 0, 0
        valid = 0

        while right < len(s):
            cur = s[right]
            right += 1
            if cur in need:
                if cur in window:
                    window[cur] += 1
                else:
                    window[cur] = 1
                if need[cur] == window[cur]:
                    valid += 1

            while right - left > len(target):
                cur = s[left]
                left += 1
                if cur in need:
                    # 只有目前计数刚好满足的字符   缩小窗口的时候才更新valid
                    if window[cur] == need[cur]:
                        valid -= 1
                    window[cur] -= 1
            # 从上边循环出来后，窗口大小正好是target长度，其实循环只执行了一次
            if valid == len(need):
                return True

        return False


s = Solution()
s.checkInclusion("trinitrophenylmethylnitramine", "dinitrophenylhydrazinetrinitrophenylmethylnitramine")
