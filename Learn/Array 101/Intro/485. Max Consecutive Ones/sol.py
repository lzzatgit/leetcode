class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        cnt = max_cnt = 0

        for num in nums:
            if num == 1:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 0

        return max(max_cnt, cnt)
