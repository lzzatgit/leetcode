class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if nums[0] <= nums[r]:
            return nums[0]

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if nums[mid-1] > nums[mid]:
                return nums[mid]

            if nums[mid] < nums[l]:
                r = mid -1
            else:
                l = mid + 1
