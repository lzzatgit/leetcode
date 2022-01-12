class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return None
        return self.quickSelect(nums, 0, n-1, n-k)


    def quickSelect(self, nums, low, high, q_smallest):
        while low <= high:
            p = self.partition(nums, low, high)
            if p == q_smallest:
                return nums[q_smallest]
            elif q_smallest < p:
                return self.quickSelect(nums, low, p-1, q_smallest)
            else:
                return self.quickSelect(nums, p+1, high, q_smallest)

    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1

        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i+1], nums[high] = nums[high], nums[i+1]

        return i + 1
