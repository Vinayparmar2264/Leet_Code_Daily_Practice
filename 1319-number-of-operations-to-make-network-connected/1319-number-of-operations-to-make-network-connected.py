
class DisjoinSet:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0]*(n+1)
        self.extra_edge = 0

    def find(self,x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,u,v):
        
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            self.extra_edge += 1
            return 

        if self.rank[pu]<self.rank[pv]:
            self.parent[pu] = pv


        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu

        else:
            self.parent[pv] = pu
            self.rank[pu] += 1


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        dsu = DisjoinSet(n)
        
        for u,v in connections:
            dsu.union(u,v)
                
        components = 0
        for i in range(n):
            if dsu.find(i) == i:
                components += 1
        print(dsu.extra_edge)
        if dsu.extra_edge >= components-1:
            return components -1 
        return -1
        
