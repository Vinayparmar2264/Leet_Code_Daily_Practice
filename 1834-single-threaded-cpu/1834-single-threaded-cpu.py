import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort()

        min_heap = []
        time = tasks[0][0]
        result = []

        i = 0
        j = 0
        n = len(tasks)

        while i < n:

            while j < n and tasks[j][0] <= time:
                heapq.heappush(min_heap, (tasks[j][1], tasks[j][2]))   # FIX
                j += 1

            if not min_heap:            # FIX for idle CPU
                time = tasks[j][0]
                continue

            processTime, idx = heapq.heappop(min_heap)
            result.append(idx)
            time += processTime
            i += 1

        return result