# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s, e = 0, n-1

        while s <= e:
            m = (s+e)//2
            # t, f, f, f ,f
            if isBadVersion(m):
                e = m -1
            else:
                s = m +1

        return s

# solved in first try once there was no syntax error
