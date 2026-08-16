class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float("inf") for _ in range(n)] for _ in range(n)]
    
    
        for u,v,w in edges:
            dist[u][v] = w
            dist[v][u] = w

        
        for i in range(n):
            dist[i][i] = 0
    

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via] != float("inf") and dist[via][j] != float("inf"):
                        dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])
        
        min_neighbors = n+1
        city = -1
        for i in range(n):
            neighbors = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    neighbors += 1
    
            if neighbors <= min_neighbors:
                node = i
                min_neighbors = neighbors

        return node
                    
