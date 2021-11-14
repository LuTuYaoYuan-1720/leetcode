class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """

        ss = s.split()
        ints = []
        for item in ss:
            if item.isdigit():
                ints.append(int(item))

        for i in range(1, len(ints) - 1):
            if ints[i] <= ints[i - 1]:
                return False

        return True

s = Solution()
s.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")

