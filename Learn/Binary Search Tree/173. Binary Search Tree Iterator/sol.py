# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._inorder_leftmost(root)

    def _inorder_leftmost(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()

        if node.right != None:
            self._inorder_leftmost(node.right) # call helper function to maintain the stack correctly
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# leetcode solution
# time O(1)
# space O(H) H is the height of the tree
