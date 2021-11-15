# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False

        cur_sum = targetSum - root.val

        while True:
            if root.left == None and root.right == None:
                return cur_sum==0
            else:
                return self.hasPathSum(root.left, cur_sum) or self.hasPathSum(root.right, cur_sum)

        self.hasPathSum(root, targetSum)
