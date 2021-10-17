import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        len_left, len_mid = len(left), len(mid)

        if k <= len_left:
            return self.findKthLargest(left, k)
        elif k > len_left + len_mid:
            return self.findKthLargest(right, k - (len_left + len_mid))
        else:
            return mid[0]
