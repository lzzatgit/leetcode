class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        return [max(nums[i:i+k]) for i in range(n-k+1)]

# leetcode Solution 1
# time: O(N**2)
