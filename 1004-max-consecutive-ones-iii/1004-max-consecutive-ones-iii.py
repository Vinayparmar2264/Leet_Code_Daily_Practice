class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi =0
        left =0
        right =0
        zeros =0
        n = len(nums)
        while right < n:
            if nums[right]==0:
                zeros+=1
            if zeros>k:
                    if nums[left]==0:
                        zeros-=1
                    left+=1
            maxi = max(maxi,right-left+1)
            right+=1
        return maxi

# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         max_ones = 0
#         zero_count = 0
#         left = 0
        
#         for right in range(len(nums)):
#             if nums[right] == 0:
#                 zero_count += 1
                
#             while zero_count > k:
#                 if nums[left] == 0:
#                     zero_count -= 1
#                 left += 1
                
#             max_ones = max(max_ones, right-left+1)
            
#         return max_ones 