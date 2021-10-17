class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in diff_dict:
                return [idx, diff_dict.get(diff)]
            else:
                diff_dict[nums[idx]] = idx
