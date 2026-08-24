"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        if not node: return None
        mp = {}

        mp[node] = Node(node.val)
        q = deque()
        q.append(node)


        while q:
            curr = q.popleft()

            for n in curr.neighbors:
                if n not in mp:
                    mp[n] = Node(n.val)
                    q.append(n)
                mp[curr].neighbors.append(mp[n])


        return mp[node]
        