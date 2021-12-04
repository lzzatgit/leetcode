class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1 #now the element that i is pointing to is guaranteed to be a duplicated elemented
                nums[i] = nums[j]

        return i + 1
