class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        chara = {')': '(', '}': '{', ']' : '['}

        for c in s:
            if c in chara:
                if stack and stack[-1] == chara[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False