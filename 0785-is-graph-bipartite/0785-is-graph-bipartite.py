class Solution:
    def bfs(self,i,color,graph,visit):
        que = deque()
        que.append(i)
        visit[i] = color

        while que:
            node = que.popleft()
            for adjNode in graph[node]:
                if visit[adjNode] == -1:
                    que.append(adjNode)
                    visit[adjNode] = 1-visit[node]
                elif visit[adjNode] == visit[node]:
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:

        visit = [-1]*len(graph)

        for i in range(len(graph)):

            if visit[i]==-1:

                ans = self.bfs(i,0,graph,visit)

                if ans == False:
                    
                    return False
                    
        return True
        