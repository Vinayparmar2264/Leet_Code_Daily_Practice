class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(1,cols):
                matrix[row][col] += matrix[row][col-1]
        
        result = 0

        for st_col in range(cols):
            for j in range(st_col,cols):
                mp = {0:1}
                cumSum = 0
                for row in range(rows):
                    cumSum += matrix[row][j] - (matrix[row][st_col-1] if st_col > 0 else 0)

                    if cumSum-target in mp :
                        result += mp[cumSum - target]
                    
                    mp[cumSum] = mp.get(cumSum,0)+1
        return result


