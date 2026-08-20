class Solution:
    def solve(self,i,amount,coins,dp):
        if amount == 0 :
            return 1
        if i < 0 or amount < 0 :
            return 0

        if dp[i][amount] != -1:
            return dp[i][amount]

        pick = self.solve(i,amount-coins[i],coins,dp)
        not_pick = self.solve(i-1,amount,coins,dp)
        dp[i][amount] =  pick + not_pick
        return dp[i][amount]

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1]*(amount+1) for _ in range(len(coins))]
        return self.solve(len(coins)-1,amount,coins,dp)
        