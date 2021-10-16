class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = [] #Initiate

        n = len(nums) # save length to aviod rep cal

        if n < 4: #corner case
            return result

        nums.sort() #sort necessary

        for i in range(n-3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target: #corner case opt
                break

            if nums[i] + nums[n-3]+ nums[n-2] + nums[n-1] < target:  #corner case opt
                continue

            if i > 0 and nums[i] == nums[i-1]: #dedup
                continue

            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:#dedup
                    continue

                #start of two pointer
                k = j + 1
                l = n-1
                while k < l:
                    tmp = nums[i] + nums[j] + nums[k] + nums[l]
                    if tmp == target:
                        result.append([nums[i],nums[j],nums[k],nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    elif tmp < target:
                        k += 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                    else:
                        l -= 1
                        while l > k and nums[l] == nums[l+1]:
                            l -= 1

        return result
