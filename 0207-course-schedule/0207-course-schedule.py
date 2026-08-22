class Solution:
    def dfs(self,node,adj,visit ,path_visit):
        visit[node] = 1
        path_visit[node] = 1
    
        for adjNode in adj[node]:
            if visit[adjNode] == 0:
               ans =  self.dfs(adjNode,adj,visit,path_visit)
               if ans == False:
                    return False
            elif path_visit[adjNode] == 1:
                return False
        
        path_visit[node] = 0
        return True
            

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            adj[v].append(u)

        visit = [0 for _ in range(numCourses)]
        path_visit = [0 for _ in range(numCourses)]
        
        for i in range(numCourses):
            if visit[i] == 0:
                if  self.dfs(i,adj,visit,path_visit) == False:
                    return False
        
        return True
