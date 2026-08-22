class Solution:
    def solve(self, i, nums, subset, lst):

        if i >= len(nums):
            lst.append(tuple(subset))
            return

        subset.append(nums[i])

        self.solve(i + 1, nums, subset, lst)

        subset.pop()

        self.solve(i + 1, nums, subset, lst)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        lst = []

        self.solve(0, nums, [], lst)

        lst = set(lst)

        return [list(x) for x in lst]