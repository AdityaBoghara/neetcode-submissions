class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            premap[c].append(p)


        visited = set() 
        complete = set() 
        def dfs(crs): 
            if crs in visited: 
                return False 
            if crs in complete: 
                return True 
            visited.add(crs) 
            
            for p in premap[crs]: 
                if p not in complete: 
                    if not dfs(p): 
                        return False 
                        
            visited.remove(crs) 
            complete.add(crs) 
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        