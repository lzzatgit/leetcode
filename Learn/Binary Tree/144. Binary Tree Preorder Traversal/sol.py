class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, order = [root], []

        while stack:
            node = stack.pop()
            if not node:
                continue

            order.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

        return order
