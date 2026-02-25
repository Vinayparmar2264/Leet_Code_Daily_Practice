class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        count =1
        ans = [-1]*(len(nums)-k+1)
        for i in range(1,k):
            if nums[i]==nums[i-1]+1:
                count+=1
            else:
                count=1
        if count==k:
            ans[0]=nums[k-1]
        i=1
        j=k
        while j<len(nums):
            if nums[j]==nums[j-1]+1:
                count+=1
            else:
                count=1
            if count>=k:
                ans[i]=nums[j]
            
            j+=1   
            i+=1
        return ans 
        
