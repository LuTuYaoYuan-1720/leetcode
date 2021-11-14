from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_str = ''
        for num in digits:
            digit_str += str(num)

        num_plus_one = int(digit_str) + 1

        num_plus_one_str = str(num_plus_one)

        res = []
        for char in num_plus_one_str:
            res.append(int(char))

        return res


s = Solution()
print(s.plusOne([1, 2, 3]))
