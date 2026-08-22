class Solution:

    def solve(self, i, nums, subset, ans):

        ans.append(subset[:])

        for j in range(i, len(nums)):

            if j > i and nums[j] == nums[j - 1]:
                continue

            subset.append(nums[j])

            self.solve(j + 1, nums, subset, ans)

            subset.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        ans = []

        self.solve(0, nums, [], ans)

        return ans