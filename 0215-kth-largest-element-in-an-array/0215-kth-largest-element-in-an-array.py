import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # min_heap = nums[:k]
        
        # heapq.heapify(min_heap)

        min_heap = []

        for i in range(k):
            heapq.heappush(min_heap,nums[i])
        
        for num in nums[k:]:
            
            if num > min_heap[0] :
                
                heapq.heappushpop(min_heap,num)
            
        return min_heap[0]