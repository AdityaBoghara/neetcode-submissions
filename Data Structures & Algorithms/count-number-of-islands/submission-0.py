from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        count = 0

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            visited.add((i, j))

            while q:
                row, col = q.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    if (
                        0 <= new_row < M
                        and 0 <= new_col < N
                        and grid[new_row][new_col] == "1"
                        and (new_row, new_col) not in visited
                    ):
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))

        M, N = len(grid), len(grid[0])

        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    bfs(i, j)

        return count

        