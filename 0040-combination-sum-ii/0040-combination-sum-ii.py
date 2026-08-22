class Solution:
    def solve(self,i,candidates,target,path,subset):
        if target == 0 :
            subset.append(path[:])
            return
        
        for j in range(i,len(candidates)):

            if j>i and candidates[j] == candidates[j-1]:
                continue

            if target<0:
                break

            path.append(candidates[j])

            self.solve(j+1,candidates,target-candidates[j],path,subset)

            path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        subset = []

        self.solve(0,candidates,target,[],subset)

        return subset