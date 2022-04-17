class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        i = 0
        while i < len(s):
            if s[i:i + 1] == "X":
                count += 1
                i += 3
                continue
            i += 1

        return count


s = Solution()
print(s.minimumMoves("XXX"))
print(s.minimumMoves("XXOX"))
print(s.minimumMoves("OOOO"))
