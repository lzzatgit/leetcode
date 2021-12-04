class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        #detect the start of the valley:
        while i < len(arr) - 1 and arr[i+1] - arr[i] > 0:
            i+=1

        if i == 0: # after found start of the valley i, make sure it is not start point, which means no increasing part
            return False

        j = i
        while j < len(arr) - 1 and arr[j+1] - arr[j] < 0:
            j+=1

        # after find the end j, make sure 1 no more ele after it; 2. j != i so that the descreasing part exist
        if j == len(arr) - 1 and j != i:
            return True
        else:
            return False
# time O(N) two while loops but loop the array only once
# space O(1) two variables i and j
