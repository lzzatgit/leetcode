# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        while root != None:
            if root.val == val:
                return root
            if root.val > val:
                root = root.left
            else:
                root = root.right
        return None

# time O(H) H is the height of the Tree
# space O(1) cause no additional data structure used to store
