from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.bfs(grid, i , j)
        return count

    def bfs(self, grid, i, j):
        queue = deque([(i, j)])
        grid[i][j] = '@'

        while queue:
            i, j = queue.popleft()
            for delta_i, delta_j in [(1, 0), (-1,0), (0, 1), (0, -1)]:
                new_i = i + delta_i
                new_j = j + delta_j
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]) or grid[new_i][new_j] != '1':
                    continue
                queue.append((new_i, new_j))
                grid[new_i][new_j] = '@'
    
