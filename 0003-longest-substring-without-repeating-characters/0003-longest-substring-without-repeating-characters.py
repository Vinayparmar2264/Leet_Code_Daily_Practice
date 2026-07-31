class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lastSeen = {}

        left = 0
        longest = 0

        for right in range(len(s)):

            if s[right] in lastSeen and lastSeen[s[right]] >= left:
                left = lastSeen[s[right]] + 1

            lastSeen[s[right]] = right

            longest = max(longest, right - left + 1)

        return longest