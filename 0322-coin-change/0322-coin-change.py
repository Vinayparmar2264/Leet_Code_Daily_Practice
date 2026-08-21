class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def solve(i,temp,dp):
            if temp == amount:
                return 0

            if i >= len(coins) or temp > amount:
                return float("inf")
            
            if dp[i][temp] != -1:
                return dp[i][temp]

            pick = 1 + solve(i,temp+coins[i],dp)
            not_pick = solve(i+1,temp,dp)
            
            dp[i][temp] =  min(pick,not_pick)
            return dp[i][temp]


        n = len(coins)

        dp = [[-1]*(amount+1) for _ in range(n)]

        x = solve(0,0,dp)
        if x == float("inf"):
            return -1
        return x
     