class Solution:
    def solve(self,nums,temp,st,result):
        if len(temp) == len(nums):
            result.append(list(temp))
            return
        
        for i in range(len(nums)):
            if  nums[i] not in st:
                temp.append(nums[i])
                st.add(nums[i])
                self.solve(nums,temp,st,result)
                temp.pop()
                st.remove(nums[i])

        
    def permute(self, nums: List[int]) -> List[List[int]]:
        st = set()
        result = []
        self.solve(nums,[],st,result)
        return result