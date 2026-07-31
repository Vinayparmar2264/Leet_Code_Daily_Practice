class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        
        i = 0
        ans = 0

        for j in range(len(s)):
            while s[j] in myset:
                myset.remove(s[i])
                i += 1
            
            myset.add(s[j])
            ans = max(ans, j - i + 1)

        return ans
