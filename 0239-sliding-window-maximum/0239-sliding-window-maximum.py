
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

#         # max_heap = []
#         # result = []

#         # for i in range(len(nums)):

#         #     heapq.heappush(max_heap, (-nums[i], i))

#         #     while max_heap[0][1] <= i-k:
#         #         heapq.heappop(max_heap)

#         #     if i >= k-1:
#         #         result.append(-max_heap[0][0])
                
#         # return result
#         que = deque()
#         result = []
#         for i in range(len(nums)):
            
#             while que and que[0] <= i - k:
#                 que.popleft()

#             while que and nums[que[0]] <= nums[i]:
#                 que.pop()

#             que.append(i)

#             if  i >= k-1 :
#                 result.append(nums[que[0]])
        
#         return result


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        que = deque()
        result = []

        for i in range(len(nums)):

            # Remove elements outside the window
            while que and que[0] <= i - k:
                que.popleft()

            # Remove smaller elements from the BACK
            while que and nums[que[-1]] <= nums[i]:
                que.pop()

            # Add current index
            que.append(i)

            # Window is ready
            if i >= k - 1:
                result.append(nums[que[0]])

        return result