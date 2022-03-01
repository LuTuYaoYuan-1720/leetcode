# coding:utf-8
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cnt = dict()

        for i in range(len(nums)):
            if nums[i] in cnt.keys():
                cnt[nums[i]].append(i)
            else:
                cnt[nums[i]] = [i]
            if len(cnt[nums[i]]) > 1:
                if cnt[nums[i]][-1] - cnt[nums[i]][-2] <= k:
                    return True

        return False


s = Solution()
print(s.containsNearbyDuplicate(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 9], k=3))
