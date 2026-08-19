from collections import deque

class Solution:

    def bfs(self, i, adjMatrix, visited):
        queue = deque([i])
        visited[i] = True

        while queue:
            node = queue.popleft()

            for x in range(len(adjMatrix)):
                if adjMatrix[node][x] == 1 and not visited[x]:
                    visited[x] = True
                    queue.append(x)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = [False] * n
        ans = 0

        for i in range(n):
            if not visited[i]:
                self.bfs(i, isConnected, visited)
                ans += 1

        return ans