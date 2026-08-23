class Solution:

    def mergeArr(self, left, mid, right, nums):

        count = 0

        # Count reverse pairs
        r = mid + 1

        for l in range(left, mid + 1):

            while r <= right and nums[l] > 2 * nums[r]:
                r += 1

            count += r - (mid + 1)

        # Normal merge
        temp = []

        l = left
        r = mid + 1

        while l <= mid and r <= right:

            if nums[l] <= nums[r]:
                temp.append(nums[l])
                l += 1

            else:
                temp.append(nums[r])
                r += 1

        while l <= mid:
            temp.append(nums[l])
            l += 1

        while r <= right:
            temp.append(nums[r])
            r += 1

        for i in range(left, right + 1):
            nums[i] = temp[i - left]

        return count

    def mergeSort(self, l, r, nums):

        if l >= r:
            return 0

        mid = l + (r - l) // 2

        count = 0

        count += self.mergeSort(l, mid, nums)

        count += self.mergeSort(mid + 1, r, nums)

        count += self.mergeArr(l, mid, r, nums)

        return count

    def reversePairs(self, nums):
        return self.mergeSort(0, len(nums) - 1, nums)