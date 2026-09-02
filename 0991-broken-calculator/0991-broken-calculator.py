class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        start = startValue

        step = 0
        while start < target:

            if target > start and target%2 == 0 :
                target //= 2
            

            else:
                target += 1

            step += 1
        return step + (start-target)