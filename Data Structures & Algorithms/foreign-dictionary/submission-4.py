class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break


        state = {} #0=unvisited, 1=in current cycle 2 = processed
        res = []


        def dfs(c):
            if c in state:
                if state[c] == 1:
                    return False
                if state[c] == 2:
                    return True
            state[c] = 1


            for n in adj[c]:
                if not dfs(n):
                    return False

            state[c] = 2
            res.append(c)
            return True

        for c in adj:
            if not dfs(c):
                return ""

        res.reverse()
        return "".join(res)
                