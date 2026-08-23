class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        cumilative_sum = 0
        result = 0

        for i in range(len(nums)):
            cumilative_sum += nums[i]
            if cumilative_sum - k in mp:
                result += mp[cumilative_sum-k]
            mp[cumilative_sum] = mp.get(cumilative_sum,0)+1
        return result

