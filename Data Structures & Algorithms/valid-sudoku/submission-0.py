class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                box = (r // 3, c // 3)
                val = board[r][c]
                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)

        return True
