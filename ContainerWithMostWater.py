class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force approach
        # max_area=0
        # for i in range(len(height)):
        #     for j in range(i,len(height)):
        #         area = min(height[i],height[j])*(j-i)
        #         max_area = max(area,max_area)
        # return max_area

        max_area =0
        i=0
        j=len(height)-1
    
        while i<j:
            max_area = max(max_area,min(height[i],height[j])*(j-i))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area
