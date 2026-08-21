class Solution:
    def isPalindrome(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l += 1
            r -= 1
        return True

    def solve(self,idx,s,n,path,result):
        if idx >= n:
            result.append(path[:])
            return
        for i in range(idx,n):
            if self.isPalindrome(s,idx,i):
                path.append(s[idx:i+1])
                self.solve(i+1,s,n,path,result)
                path.pop()

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        self.solve(0,s,n,[],result)
        return result

        