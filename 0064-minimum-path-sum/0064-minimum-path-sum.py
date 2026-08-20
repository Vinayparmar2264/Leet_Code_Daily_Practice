class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dist = [[float("inf")]*cols for _ in range(rows)]
        que = deque()
        que.append((0,0,grid[0][0]))
        dist[0][0] = grid[0][0]
        while que:
            i,j,d = que.popleft()
            for x,y in [[1,0],[0,1]]:
                new_x,new_y = i+x, j+y
                if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                    continue
                dist_trav = d + grid[new_x][new_y]
                if dist[new_x][new_y] > dist_trav :
                    dist[new_x][new_y] = dist_trav
                    que.append((new_x,new_y,dist_trav))
        return dist[rows-1][cols-1]