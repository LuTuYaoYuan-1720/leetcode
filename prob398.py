# coding:utf-8
from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.num_indices = {}
        for i, num in enumerate(nums):
            if num in self.num_indices:
                self.num_indices[num].append(i)
            else:
                self.num_indices[num] = [i]

    def pick(self, target: int) -> int:
        idx = random.randint(0, len(self.num_indices[target]) - 1)

        return self.num_indices[target][idx]


for i in range(20):
    print(random.randint(0, 10))
