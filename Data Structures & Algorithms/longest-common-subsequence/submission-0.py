class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)

        
        dp = [[0]*(len(text2)+1) for x in range(len(text1)+1)]

        for r in range(1, len(text1)+1):
            for c in range(1, len(text2)+1):
                if text1[r-1] == text2[c-1]:
                    dp[r][c] = 1 + dp[r-1][c-1]
                else:
                    dp[r][c] = max(dp[r][c - 1], dp[r - 1][c])


        return dp[len(text1)][len(text2)]


        