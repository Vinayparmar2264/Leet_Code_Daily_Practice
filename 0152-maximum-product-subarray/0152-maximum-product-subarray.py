class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        right = 1


        max_prod = float("-inf")
        for i in range(n):
            if left == 0:
                left = 1
            if right == 0:
                right = 1
                
            left *= nums[i]
            right *= nums[n-i-1]

            prod = max(left,right)
            max_prod = max(prod,max_prod)
        return max_prod
