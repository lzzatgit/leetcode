# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n

        while l < r:
            mid = (l + r) // 2

            if isBadVersion(mid) == 1:
                r = mid
            else: # isBadVersion(mid) != 1:
                l = mid + 1
        return l
