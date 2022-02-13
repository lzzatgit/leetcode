# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}
        visited = set()
        res = []

        def buildMap(parent):
            if parent.left:
                graph[parent.left] = parent
                buildMap(parent.left)
            if parent.right:
                graph[parent.right] = parent
                buildMap(parent.right)

        def findNode(node, k):
            if not node or (node in visited):
                return
            visited.add(node)

            if k == 0:
                res.append(node.val)

            findNode(node.left, k-1)
            findNode(node.right, k-1)
            if node in graph:
                findNode(graph[node], k-1)

        buildMap(root)
        findNode(target, k)
        return res
