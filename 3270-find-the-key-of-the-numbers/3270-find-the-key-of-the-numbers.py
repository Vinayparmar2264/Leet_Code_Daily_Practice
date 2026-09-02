class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        key = 0
        count = 0
        while num1 or num2 or num3:
            rem1  = num1%10
            rem2 = num2 % 10
            rem3 = num3 % 10
            rem = min (rem1,rem2,rem3)
            key = key + rem*(10**count)
            count +=1 
            num1 //= 10
            num2 //= 10
            num3 //= 10
        return key
