class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        total_prime_setBits = 0
        for num in range(left,right+1):
            count =0
            while num>0:
                rem=num%2
                if rem==1:
                    count+=1
                num = num//2

            print(count)
            if count==1:
                continue
            temp = 2
            while temp<= count**0.5:
                if count%temp==0:
                    break
                temp+=1
            else:
                total_prime_setBits+=1
        return total_prime_setBits
                

            

