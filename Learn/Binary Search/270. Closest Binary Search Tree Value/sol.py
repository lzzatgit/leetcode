# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closet = root.val

        while root:
            closet = min(root.val, closet, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closet
