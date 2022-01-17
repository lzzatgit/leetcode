class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0 , len(matrix)
        res = []

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for j in range(top, bottom):
                res.append(matrix[j][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for k in reversed(range(left, right)):
                res.append(matrix[bottom-1][k])
            bottom -= 1

            for l in reversed(range(top, bottom)):
                res.append(matrix[l][left])
            left += 1

        return res
