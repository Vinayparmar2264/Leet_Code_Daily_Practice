class Solution:

    def solve(self, idx, s, wordDict,dp):

        # Entire string has been successfully consumed
        if idx >= len(s):
            return True

        if dp[idx] != -1:
            return dp[idx]
        
        if s in wordDict :
            return True

        for i in range(idx, len(s)):

            # Take substring s[idx...i]
            if s[idx:i+1] in wordDict:

                # If remaining string can also be broken
                if self.solve(i + 1, s, wordDict,dp):
                    dp[idx] = True
                    return dp[idx]

        # No valid partition worked
        dp[idx] = False
        return dp[idx]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [-1]*len(s)
        return self.solve(0, s, wordDict,dp)