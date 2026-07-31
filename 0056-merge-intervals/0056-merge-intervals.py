class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        ans.append(intervals[0])

        for i in range(1,len(intervals)):

            start = ans[-1][0]
            end = ans[-1][1]
            new_start = intervals[i][0]
            new_end = intervals[i][1]

            if end >= new_start :
                if end < new_end:
                    ans[-1][1] = new_end
            else:
                ans.append(intervals[i])

        return ans


            