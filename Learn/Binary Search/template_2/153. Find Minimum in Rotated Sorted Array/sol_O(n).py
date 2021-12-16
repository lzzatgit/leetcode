class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums += nums[0:1]
        # find the starting point:
        for i in range(1, len(nums)):
            slope = nums[i] - nums[i-1]
            if slope > 0:
                continue
            if slope < 0:
                break
        if i == len(nums) - 1:
            return nums[0]

        return nums[i]
