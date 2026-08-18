class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #n  = len(nums)
        # new_k = k%n
        # nums[:] = nums[n-new_k:n] + nums[0:n-new_k]
        # return nums

        n = len(nums)    
        new_k = k%n
        left= n-new_k
        right=n-1
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left +=  1
            right -= 1

        left = 0
        right = n-new_k-1
     
        while left < right :
            nums[left],nums[right] = nums[right],nums[left]
            left +=  1
            right -= 1


        left = 0
        right = n-1
        while left < right :
            nums[left],nums[right] = nums[right],nums[left]
            left +=  1
            right -= 1

        return nums    
            

            
              

