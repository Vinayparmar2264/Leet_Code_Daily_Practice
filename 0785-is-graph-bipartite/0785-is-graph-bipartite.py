class Solution:
    def dfs(self,node,color,graph,visit):

        visit[node] = color

        for adjNode in graph[node]:

            if visit[adjNode] != color and visit[adjNode] == -1:

                ans = self.dfs(adjNode,1-color,graph,visit)

                if ans == False:

                    return False
                    
            elif visit[adjNode] == color:

                return False
                
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:

        visit = [-1]*len(graph)

        for i in range(len(graph)):

            if visit[i]==-1:

                ans = self.dfs(i,0,graph,visit)

                if ans == False:
                    
                    return False
                    
        return True
        