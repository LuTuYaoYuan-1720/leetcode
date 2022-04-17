# coding:utf-8
import random


class RandomizedSet:

    def __init__(self):
        self.nums = {}

    def insert(self, val: int) -> bool:
        if val not in self.nums:
            self.nums[val] = 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.nums:
            self.nums.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        keys = self.nums.keys()
        return list(self.nums.keys())[random.randint(0, len(keys) - 1)]
