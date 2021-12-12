class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        res = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1

            elif nums1[i] > nums2[j]:
                j += 1

            else:
                if len(res) == 0 or res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1
        return res

# According to comment 1, facebook interview question, the additional conditions are that nums1 and nums2 are sorted
# requirement is that time O(n) and O(1) space (returned the result is not taken into consideration to the space)

# time O(n) not take sort into consideration
# space O(1) only constant variables are created except for res

# key point of this problem is how to deal with the duplication without use hashtable or set
