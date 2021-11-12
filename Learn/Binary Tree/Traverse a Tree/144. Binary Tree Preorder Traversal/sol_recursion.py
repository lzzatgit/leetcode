# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(root):
            if root == None:
                return None
            res.append(root.val)
            if root.left != None:
                preorder(root.left)
            if root.right != None:
                preorder(root.right)

        preorder(root)
        return res
