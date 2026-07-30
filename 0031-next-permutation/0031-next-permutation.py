class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # Step 1: Find the pivot
        pivot = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        # Step 2: Find the rightmost element greater than pivot
        if pivot != -1:
            for j in range(n - 1, pivot, -1):
                if nums[j] > nums[pivot]:
                    nums[pivot], nums[j] = nums[j], nums[pivot]
                    break

        # Step 3: Reverse the suffix
        left = pivot + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1