# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def bft(root, low=float('-inf'),  high = float('inf')):
            if root == None:
                return True

            if root.val <= low or root.val >= high:
                return False

            return bft(root.left, low, root.val) and bft(root.right, root.val, high)

        return bft(root)

# leetcode Solution
# time O(n)
# space O(n)
