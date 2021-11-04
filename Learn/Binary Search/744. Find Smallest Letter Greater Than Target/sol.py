class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if len(letters) == 0:
            return None
        l = 0
        r = len(letters) - 1
        while l <= r:
            mid = (l + r) // 2
            if letters[mid] > target:
                if target > letters[mid-1]:
                    return letters[mid]
                r = mid - 1
            else:
                if mid+1 < len(letters) and target < letters[mid+1]:
                    return letters[mid+1]
                l = mid + 1
        return letters[0]
