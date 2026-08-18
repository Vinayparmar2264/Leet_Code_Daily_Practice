class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        
        nums[::-1] =  nums[n-k-1::-1] + nums[:n-k-1:-1] 
        # print(nums[::-1])
        