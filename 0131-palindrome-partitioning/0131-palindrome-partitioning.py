class Solution:
    def isPal(self,s,l,r):
        while l<r :
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

    def solve(self,i,s,pal,ans):
        if i>=len(s):
            ans.append(pal[:])
            return
        
        for  j in range(i,len(s)):
            if self.isPal(s,i,j):
                pal.append(s[i:j+1])
                self.solve(j+1,s,pal,ans)
                pal.pop()

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.solve(0,s,[],ans)
        return ans