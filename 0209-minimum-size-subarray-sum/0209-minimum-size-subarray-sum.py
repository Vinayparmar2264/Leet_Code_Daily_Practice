class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float("inf")
        left = 0
        curr = 0
        for right in range(len(nums)):
            curr += nums[right]
            if curr >= target:
                while left <= right  and  curr >= target:
                    min_size = min(min_size, right - left + 1)
                    curr -= nums[left]
                    left += 1

        return min_size if min_size != float("inf") else 0 