class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen_eles = []
        i = 0

        while i <len(arr):
            if self.binarySearch(seen_eles, arr[i]*2) == 1:
                return True
            if arr[i]%2 == 0 and self.binarySearch(seen_eles, arr[i]/2)==1:
                return True
            seen_eles.append(arr[i])
            i += 1

        return False

    def binarySearch(self, array, num): # time O(logn)
        array.sort()
        if len(array) == 0:
            return -1

        l, r = 0, len(array)-1
        while l <= r:
            mid = (l + r) // 2
            if array[mid] == num:
                return 1
            elif array[mid] < num:
                l = mid + 1
            else:
                r = mid - 1
        return -1

# time O(nlogn) while loop * binary search
# space O(n)
