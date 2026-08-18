
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        n = len(grid)
        m = len(grid[0])
        que = deque()
        que.append((0,0))
        dist = [[float("inf")]*m for _ in range(n)]
        dist[0][0] = 1
        while que :
            i,j  = que.popleft()
            d = dist[i][j]
            for k,l in [(-1,-1),(1,1),(1,-1),(-1,1),(1,0),(0,1),(-1,0),(0,-1)]:
                x,y = i + k, j+l
                if x<0 or x >= n or y<0 or y>=m:
                    continue
                if grid[x][y] == 1:
                    continue
                if dist[x][y] > d + 1:
                    dist[x][y] = d+1
                    que.append((x,y))
        if dist[n-1][m-1] != float("inf"):
            return dist[n-1][m-1]
        return -1