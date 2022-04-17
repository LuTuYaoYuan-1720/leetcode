# coding:utf-8
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        same1 = []
        sum12 = []
        for i in range(len(list1)):
            if list1[i] in list2:
                same1.append(i)
                sum12.append(i + list2.index(list1[i]))

        minindexsum = min(sum12)
        sameindex = []
        for i in range(len(sum12)):
            if sum12[i] == minindexsum:
                sameindex.append(i)

        res = [list1[same1[index]] for index in sameindex]

        return res


s = Solution()
print(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                       ["KFC", "The Grill at Torrey Pines", "Tapioca Express", "Shogun"]))
