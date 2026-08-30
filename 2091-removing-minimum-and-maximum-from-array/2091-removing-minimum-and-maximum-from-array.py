class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_idx = (0,nums[0])
        max_idx = (0,nums[0])
        for i in range(1,len(nums)):
            if nums[i] > max_idx[1]:
                max_idx = (i,nums[i])
            if nums[i] < min_idx[1]:
                min_idx = (i,nums[i])

        min_idx = min_idx[0]
        max_idx = max_idx[0]
        # print(min_idx,max_idx)

        min_del = min(min_idx,max_idx)
        max_del = max(min_idx,max_idx)
        # print(min_del,max_del)

        left = max_del +1
        right = len(nums)-min_del
        both = (min_del + 1 + len(nums)-max_del)
        # print(left,right,both)
        return min(left,right,both)
