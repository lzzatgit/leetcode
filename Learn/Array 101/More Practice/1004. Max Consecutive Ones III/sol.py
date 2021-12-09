class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        num_zeros = 0
        res = 0

        for r in range(len(nums)):
            num_zeros += 1 - nums[r] #等于if nums[r] == 0: num_zeros += 1

            if num_zeros > k:
                num_zeros -= 1 - nums[l] #等于 if nums[l] == 0: num_zeros -= 1
                l += 1

            res = max(res, r-l+1)
        return res
# https://www.youtube.com/watch?v=LNyGd9JxPCs
# time O(N)
# space O(1)
