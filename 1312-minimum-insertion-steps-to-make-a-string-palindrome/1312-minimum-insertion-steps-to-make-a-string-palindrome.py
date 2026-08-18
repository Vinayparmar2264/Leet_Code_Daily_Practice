class Solution:
    def solve(self,i,j,s1,s2,dp):
        if i < 0 or j < 0 :
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        if s1[i] == s2[j]:
            dp[i][j] =  1 + self.solve(i-1,j-1,s1,s2,dp)
            return dp[i][j]
        dp[i][j] = max(self.solve(i-1,j,s1,s2,dp),self.solve(i,j-1,s1,s2,dp))
        return dp[i][j]
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[-1]*(n+1) for _ in range(n+1)]
        s2 = s[::-1]
        common_sequence =  self.solve(n-1,n-1,s,s2,dp)
        required = n - common_sequence
        return required