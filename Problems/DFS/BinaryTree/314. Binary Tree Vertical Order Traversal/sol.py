# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        min_col, max_col = float('inf'), float('-inf')
        col_dict = defaultdict(list)

        def dfs(node, row, col):
            nonlocal min_col, max_col
            if node:
                col_dict[col].append([row, node.val])
                min_col = min(min_col, col)
                max_col = max(max_col, col)

                # preorder traversal
                dfs(node.left, row+1, col-1)
                dfs(node.right, row+1, col+1)
            return

        dfs(root, 0, 0)

        for col in range(min_col, max_col+1):
            col_dict[col].sort(key = lambda x:x[0])
            col_lst = [val for row, val in col_dict[col]]
            res.append(col_lst)

        return res

# time O()
# space O()
