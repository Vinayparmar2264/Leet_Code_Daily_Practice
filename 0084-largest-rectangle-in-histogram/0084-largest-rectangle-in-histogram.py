class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def left_right_smaller(heights):
            n = len(heights)
            stack = []

            left_smaller = [-1]*n
            
            for i in range(n):
                while stack and stack[-1][0] >= heights[i]:
                    stack.pop()
                if stack:
                    left_smaller[i] = stack[-1][1]
                stack.append((heights[i],i))
                
            stack = []

            right_smaller = [n]*n

            for i in range(n-1,-1,-1):
                while stack and stack[-1][0] >= heights[i]:
                    stack.pop()
                if stack:
                    right_smaller[i] = stack[-1][1]
                stack.append((heights[i],i))
            return left_smaller,right_smaller
        
        left_smaller, right_smaller = left_right_smaller(heights)
    

        max_area = 0
        for i in range(len(heights)):
            width = abs(right_smaller[i] - left_smaller[i] -1 )
        
            area = width * heights[i]
            max_area = max(area,max_area)

        return max_area