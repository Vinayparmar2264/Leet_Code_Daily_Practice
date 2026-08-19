class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[-1]*(m) for _ in range(n)]
        def dfs(i,j,word1,word2,dp):
            if i >= len(word1):
                return len(word2)-j
            if j>= len(word2):
                return len(word1)-i

            if dp[i][j] != -1 :
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = dfs(i+1,j+1,word1,word2,dp)
                return dp[i][j]
            else:
                insert = dfs(i+1,j,word1,word2,dp)
                delete = dfs(i,j+1,word1,word2,dp)
                replace = dfs(i+1,j+1,word1,word2,dp)
                dp[i][j] =  1 + min(insert,delete,replace)
            return dp[i][j]

        return dfs(0,0,word1,word2,dp)