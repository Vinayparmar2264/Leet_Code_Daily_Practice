class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        visit = [[0 for _ in range(cols)] for _ in range(rows)]
    
        for i in range(rows):

            for j in range(cols):
            
                if grid[i][j] == "1" and visit[i][j]==0:
                
                    islands += 1
                    que = deque()
                    que.append((i,j))
                    visit[i][j] = 1

                    while que:
                        r,c = que.popleft()
                        for a,b in [[-1,0],[0,-1],[1,0],[0,1]]:
                            x,y = r + a, c + b
                            if x<0 or x>= rows or y<0 or y>=cols :
                                continue
                            elif visit[x][y] == 1 or grid[x][y] == "0":
                                continue
                            que.append((x,y))
                            visit[x][y] = 1
                    print(visit)
        return islands
                            