# coding:utf-8
from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        cnt = 0
        l = 0
        r = len(plants) - 1
        A, B = capacityA, capacityB

        while l < r:
            if A >= plants[l]:
                A -= plants[l]
                l += 1
            else:
                A = capacityA
                A -= plants[l]
                l += 1
                cnt += 1

            if B >= plants[r]:
                B -= plants[r]
                r -= 1
            else:
                B = capacityB
                B -= plants[r]
                r -= 1
                cnt += 1

            if l == r:
                if A >= B:
                    if A >= plants[l]:
                        A -= plants[l]
                        l += 1
                    else:
                        A = capacityA
                        A -= plants[l]
                        l += 1
                        cnt += 1
                elif B > A:
                    if B >= plants[r]:
                        B -= plants[r]
                        r -= 1
                    else:
                        B = capacityB
                        B -= plants[r]
                        r -= 1
                        cnt += 1

        return cnt


s = Solution()
s.minimumRefill(plants=[1, 2, 4, 4, 5], capacityA=6, capacityB=5)
s.minimumRefill(plants=[2, 2, 5, 2, 2], capacityA=5, capacityB=5)
