class Solution:
    def solve(self,i,candidates,target,path,subset):
        if target == 0:
            subset.append(tuple(path))
            return 
        if target < 0 :
            return 
        if i >= len(candidates):
            return 
        
        path.append(candidates[i])
        self.solve(i,candidates,target-candidates[i],path,subset)
        path.pop()
        self.solve(i+1,candidates,target,path,subset)


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        subset = []
        self.solve(0,candidates,target,[],subset)
        subset = list(set(subset))
        return subset