class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2): #make the shorter one nums1 and perform binSearch on it
            nums1, nums2 = nums2, nums1

        l = 0
        r = len(nums1) - 1

        while True:
            # find mid of both array
            i = (l + r) // 2
            j = half - (i+1) - 1 # since length vs index, so need to -1 -1

            # after split by mid i
            # Aleft: right most of left part of nums1
            # Aright: left most of right part of nums1
            # take care of index out of range
            Aleft = nums1[i] if i >= 0 else float('-inf')
            Aright = nums1[i+1] if i+1<len(nums1) else float('inf')
            Bleft = nums2[j] if j >= 0 else float('-inf')
            Bright = nums2[j+1] if j+1<len(nums2) else float('inf')

            #if found right left parts
            if Aleft <= Bright and Bleft <= Aright:
                # if odd number of element
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

# Time compleity: log(min(n, m)) since we perform binary search on the shorter array
