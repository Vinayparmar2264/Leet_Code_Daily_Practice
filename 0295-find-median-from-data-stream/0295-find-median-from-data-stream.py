import heapq

class MedianFinder:

    def __init__(self):
        self.left_max_heap = []   # max heap using negative values
        self.right_min_heap = []  # normal min heap

    def addNum(self, num: int) -> None:

        # Step 1: Insert into left max heap
        if not self.left_max_heap or num <= -self.left_max_heap[0]:
            heapq.heappush(self.left_max_heap, -num)
        else:
            heapq.heappush(self.right_min_heap, num)

        # Step 2: Balance the heaps
        if len(self.left_max_heap) > len(self.right_min_heap) + 1:
            x = -heapq.heappop(self.left_max_heap)
            heapq.heappush(self.right_min_heap, x)

        elif len(self.right_min_heap) > len(self.left_max_heap):
            x = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, -x)

    def findMedian(self) -> float:

        if len(self.left_max_heap) > len(self.right_min_heap):
            return -self.left_max_heap[0]

        return (-self.left_max_heap[0] + self.right_min_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()