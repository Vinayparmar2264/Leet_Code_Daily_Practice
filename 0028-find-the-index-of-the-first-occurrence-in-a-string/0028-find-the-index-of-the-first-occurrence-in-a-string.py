class Solution:
    def computeLps(self,needle,lps):
        m = len(needle)
        length = 0
        i = 1
        while i < m:
            if needle[i] == needle[length]:
                length +=1
                lps[i] = length
                i +=1
            else:
                if length!=0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i+=1
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        lps = [0]*m
        self.computeLps(needle,lps)

        i = 0
        j = 0
        while i<n:
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            if j == m :
                return i-m
            elif i<n and haystack[i]!= needle[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return -1

        