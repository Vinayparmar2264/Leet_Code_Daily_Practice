class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2) :
            nums1,nums2 = nums2,nums1

        n = len(nums1)
        m = len(nums2)
        low = 0
        high = n

        while low <= high :
            px = low + (high-low)//2
            py = (m+n+1)//2 - px

            # left side wale 
            x1 = nums1[px-1] if px != 0 else float("-inf")
            x2 = nums2[py-1] if py != 0 else float("-inf")

            # right side wale
            x3 = nums1[px] if px < n else float("inf")
            x4 = nums2[py]  if py<  m else float("inf")

            if x1 <= x4 and x2 <= x3 :
                if (m+n+1) % 2 == 0:
                    return max(x1,x2) #  if m+n == odd, so we will pick the max b/w last element of the nums1 and first element of nums2 in the left side . max of x1 and x2
                else:
                    # if m + n == even , so we will pick one element from left and right half and return the avg. (max(x1,x2) + min(x3,x4))/2
                    return ( max(x1,x2) + min(x3,x4) ) / 2
            
            if x1 > x4 :
                high = px-1
            elif x2 > x3 :
                low = px + 1
        return -1