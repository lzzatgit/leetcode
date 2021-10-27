class Solution: /* two pointer method */
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return None

        nums.sort()

        result = nums[0] + nums[1] + nums[-1]


        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1

            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]

                if abs(cur_sum - target) < abs(result - target):
                    result = cur_sum

                if cur_sum < target:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

        return result
