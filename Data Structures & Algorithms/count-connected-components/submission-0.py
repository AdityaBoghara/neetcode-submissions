class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for i in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        count = 0

        def dfs(node):
            visited.add(node) 
            for n in adj[node]: 
                if n in visited: 
                    continue
                else:
                    dfs(n)

        for node in range(n):
            if node not in visited:
                count+=1
                dfs(node)

        return count