class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = arr[len(arr)-1]

        for i in reversed(range(len(arr)-1)):
            val = curr_max
            curr_max = max(arr[i], curr_max)
            arr[i] = val

        arr[len(arr)-1] = -1

        return arr
