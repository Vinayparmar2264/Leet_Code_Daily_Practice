class Solution:
    def solve(self,i,j,grid,dp):
        if i >= len(grid) or j >= len(grid[0]):
            return float("inf")
        
        if i == len(grid)-1 and j == len(grid[0])-1 :
            return grid[i][j]

        if dp[i][j] != -1:
            return dp[i][j]

    
        down =  self.solve(i+1,j,grid,dp)
        right = self.solve(i,j+1,grid,dp)
        dp[i][j] = grid[i][j] + min(down,right)
        return dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[-1]*cols for _ in range(rows)]
        return self.solve(0,0,grid,dp)