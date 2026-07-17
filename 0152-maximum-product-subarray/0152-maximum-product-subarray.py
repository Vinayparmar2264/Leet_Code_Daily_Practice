class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre , suff = 1 , 1
        store = float("-inf")
        n = len(nums)
        for i in range(len(nums)):
            if pre == 0 :
                pre = 1
            if suff == 0:
                suff = 1
        
            pre *= nums[i]
            suff *= nums[n-i-1]
            store = max(store, max(pre, suff))

        return store