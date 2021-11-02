class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]

        start = self.binarySearch(nums, target, True)
        end = self.binarySearch(nums, target, False)

        return [start, end]

    def binarySearch(self, nums, target, left):
        l = 0
        r = len(nums) - 1
        i = -1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                i = mid
                if left:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return i
