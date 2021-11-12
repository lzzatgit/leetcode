# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [], []

        while True:
            while root:
                stack.append(root) #这里是append root
                root = root.left
            if not stack:
                return res
            root = stack.pop()
            res.append(root.val) #这里是append root.val
            root = root.right

# time O(n)
# space O(n)
# because we need to access every node for 1 time
