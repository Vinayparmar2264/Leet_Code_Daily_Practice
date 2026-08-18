class Solution:
    def solve(self,i,j,s,dp):
        if i>j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        if s[i] == s[j]:
            dp[i][j] = self.solve(i+1,j-1,s,dp)
            return dp[i][j]
        dp[i][j] = 1 + min (self.solve(i+1,j,s,dp),self.solve(i,j-1,s,dp))
        return dp[i][j]

    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[-1]*(n+1) for _ in range(n+1)]
        return self.solve(0,len(s)-1,s,dp)
        