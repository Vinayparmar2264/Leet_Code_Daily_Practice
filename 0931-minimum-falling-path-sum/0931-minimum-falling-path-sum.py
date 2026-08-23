class Solution:
    def solve(self,i,j,matrix,dp):
        if i >= len(matrix) or j >= len(matrix) or j<0:
            return float("inf")
        if i == len(matrix)-1 :
            return matrix[i][j]

        if dp[i][j]  != float("inf"):
            return dp[i][j]

        down = matrix[i][j] + self.solve(i+1,j,matrix,dp)
        left_d = matrix[i][j] + self.solve(i+1,j-1,matrix,dp)
        right_d = matrix[i][j] + self.solve(i+1,j+1,matrix,dp)
        dp[i][j] =  min(down,left_d,right_d)
        return dp[i][j]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        min_path_sum = float("inf")
        dp = [[float("inf")]*len(matrix) for _ in range(len(matrix))]
        for j in range(len(matrix)):
            min_path_sum = min(min_path_sum,self.solve(0,j,matrix,dp))
        return min_path_sum