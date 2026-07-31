class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      
        answer=-2147483647
        current=0
        for num in nums:
            current = max(num,current+num)
            answer = max(answer,current)
        return answer


# kadane's algorithm