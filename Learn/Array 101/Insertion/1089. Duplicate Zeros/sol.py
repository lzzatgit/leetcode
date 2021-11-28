class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr_len = len(arr)
        i = 0

        while i < arr_len:
            if arr[i] == 0:
                for j in reversed(range(i+1, arr_len)):
                    arr[j] = arr[j-1]
                i += 2
            else:
                i += 1

# time O(N)
# space O(1)
