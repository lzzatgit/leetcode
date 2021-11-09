# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [root]

        while len(queue) > 0: # if queue is not empty
            # each while loop is one level
            cur_level = []
            qsize = len(queue)
            for i in range(qsize): # each for loop is each node in that level
                node = queue.pop(0)
                cur_level.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            res.append(cur_level)
        return res

# method: https://www.youtube.com/watch?v=sFDNL6r5aDM
# time: O(n)
# space: O(n)
# because we need to traverse every node in the queue
