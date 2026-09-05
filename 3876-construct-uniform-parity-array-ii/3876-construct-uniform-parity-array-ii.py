class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums = sorted(nums1)

        found_odd = False
        min_odd = float('inf')
        min_even = float('inf')

        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                min_odd = nums[i]
                found_odd = True
                break
            else:
                min_even = min(min_even, nums[i])

        if not found_odd:
            return True
        
        

        return min_odd < min_even
                
                
