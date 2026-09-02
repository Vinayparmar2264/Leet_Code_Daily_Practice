class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort()
        
        print(tasks)
        min_heap = []

        time = tasks[0][0]
        
        result = []
        
        i = 0
        j = 0
        while i < len(tasks):
            
            while j < len(tasks) and  time >= tasks[j][0]:
                heapq.heappush(min_heap,(tasks[j][1],tasks[j][2]))
                j += 1
            if not min_heap:
                time = tasks[j][0]
                continue
            temp = heapq.heappop(min_heap)
            result.append(temp[1])
            time += temp[0]
            i+=1


        return result