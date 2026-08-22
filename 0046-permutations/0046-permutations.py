class Solution:
    def solve(self,idx,nums,result):
        if idx >= len(nums):
            result.append(nums[:])
            return
        
        for i in range(idx,len(nums)):
            nums[idx],nums[i] = nums[i],nums[idx]
            self.solve(idx+1,nums,result)
            nums[idx],nums[i] = nums[i],nums[idx]
   

        
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        result = []
        self.solve(0,nums,result)
        return result