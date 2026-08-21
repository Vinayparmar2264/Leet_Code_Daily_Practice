class Solution:
    def jobScheduling(self, startTime, endTime, profit):

        jobs = sorted(zip(startTime, endTime, profit))

        n = len(jobs)

        st = [x[0] for x in jobs]
        et = [x[1] for x in jobs]
        pt = [x[2] for x in jobs]

        from bisect import bisect_left

        dp = [-1] * n

        def solve(i):

            if i >= n:
                return 0

            if dp[i] != -1:
                return dp[i]

            next_job = bisect_left(st, et[i])

            pick = pt[i] + solve(next_job)

            not_pick = solve(i + 1)

            dp[i] = max(pick, not_pick)

            return dp[i]

        return solve(0)