class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # 1. Build Trie
        root = TrieNode()

        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            node.isWord = True
            node.word = word


        ROWS = len(board)
        COLS = len(board[0])

        visited = set()
        res = set()


        # 2. DFS through board + Trie together
        def dfs(r, c, node):

            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return

            char = board[r][c]

            # Move forward in Trie
            node = node.children[char]

            visited.add((r, c))

            # Found a complete word
            if node.isWord:
                res.add(node.word)

            # Explore neighbors
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            # Backtrack
            visited.remove((r, c))


        # 3. Every board cell can potentially start a word
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return list(res)