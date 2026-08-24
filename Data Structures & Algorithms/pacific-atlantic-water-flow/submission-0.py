class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        M, N = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(i, j, visited, prevHeight):
            if (
                (i, j) in visited
                or i < 0
                or j < 0
                or i == M
                or j == N
                or heights[i][j] < prevHeight
            ):
                return

            visited.add((i, j))
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])

        for c in range(N):
            dfs(0, c, pacific, 0)
            dfs(M - 1, c, atlantic,0)

        for r in range(M):
            dfs(r, 0, pacific, 0)
            dfs(r, N - 1, atlantic, 0)
           

        res = []
        for r in range(M):
            for c in range(N):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res 
