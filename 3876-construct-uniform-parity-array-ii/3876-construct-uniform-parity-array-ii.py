class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        odd = False
        even = False

        left_min = [float("inf")]*len(nums1)
        right_min = [float("inf")]*len(nums1)
        stack = []

        for i in range(len(nums1)-1,-1,-1):
            while stack and stack[-1]>nums1[i]:
                stack.pop()
            if stack:
                right_min[i] = stack[-1]
            stack.append(nums1[i])
            if not odd and  nums1[i] % 2 == 1:
                odd = True
            if not even and nums1[i] % 2 == 0 :
                even = True
        
        if not odd or not even :
            return True

        stack = []

        for i in range(len(nums1)):
            while stack and stack[-1] > nums1[i] :
                stack.pop()
            if stack:
                left_min[i] = stack[-1]
            stack.append(nums1[i])


        print(left_min)
        print(right_min)


        left = 0

        while left < len(nums1):

            if nums1[left]%2 == 1 :
                left += 1
                continue

            elif nums1[left]%2 == 0:
                if left_min[left] < nums1[left] or right_min[left] < nums1[left]:
                    left += 1
                    continue
                else:
                    return False
    
        return True