class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        n, i, j = len(nums), -1, -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                i, j  = mid, mid
                while i - 1 >= 0 and nums[i-1] == target:
                    i -= 1
                while j + 1 < n and nums[j+1] == target:
                    j += 1
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return [i, j]
