from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        que = deque([])
        result = []

        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)
        
        while que :
            node  = que.popleft()
            result.append(node)
            for adjNode in adj[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    que.append(adjNode)
        if len(result) == numCourses:
            return True
        return False
