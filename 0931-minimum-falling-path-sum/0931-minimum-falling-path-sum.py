class Solution:

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)

        dp = [[float("inf")] * n for _ in range(n)]

        # Base case: last row
        for j in range(n):
            dp[n - 1][j] = matrix[n - 1][j]

        # Bottom to top
        for i in range(n - 2, -1, -1):

            for j in range(n):

                down = dp[i + 1][j]

                left = float("inf")
                if j > 0:
                    left = dp[i + 1][j - 1]

                right = float("inf")
                if j < n - 1:
                    right = dp[i + 1][j + 1]

                dp[i][j] = matrix[i][j] + min(
                    down,
                    left,
                    right
                )

        return min(dp[0])