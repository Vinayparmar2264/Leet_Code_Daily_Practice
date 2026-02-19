class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev_group_len = 0
        cur_group_len = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur_group_len += 1
            else:
                ans += min(prev_group_len, cur_group_len)
                prev_group_len = cur_group_len
                cur_group_len = 1
        
        ans += min(prev_group_len, cur_group_len)
        
        return ans
