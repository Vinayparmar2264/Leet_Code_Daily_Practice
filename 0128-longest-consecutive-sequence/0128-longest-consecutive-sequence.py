class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
    
        max_cons = 0
        for num in my_set:
            if num-1 not in my_set:
                count = 0
                while num in my_set:
                    num = num+1
                    count += 1
                max_cons = max(max_cons,count)
        return max_cons