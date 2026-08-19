class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 :
            return nums[0]
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low+(high-low)//2
            if mid == 0 and nums[mid+1] != nums[mid]:
                return nums[mid]
            elif mid == n-1 and nums[mid-1] != nums[mid]:
                return nums[mid]
            elif nums[mid-1] != nums[mid] and nums[mid+1] != nums[mid]:
                return nums[mid]
            if mid>0 and ( nums[mid-1] != nums[mid] and mid%2 != 0) or (nums[mid-1]==nums[mid] and mid%2 == 0) :
                high = mid -1
            else:
                low = mid+1
        
