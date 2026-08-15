class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                nse = i # next smallest element's idex
                top = stack.pop() # top element 
                pse = stack[-1] if stack else -1  # previous smallest element's index
                area = heights[top]*(nse - pse - 1)
                max_area = max(max_area,area)
            stack.append(i)
        
        while stack:
            nse = len(heights)
            top = stack.pop()
            pse = stack[-1] if stack else -1
            area = heights[top] * (nse - pse -1)
            max_area = max(max_area,area)
            
        return max_area