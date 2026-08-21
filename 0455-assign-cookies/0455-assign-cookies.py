class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        size = min(len(g),len(s))
        g.sort()
        s.sort()
        i = 0
        j = 0
        max_child = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                max_child += 1
                i += 1
                j += 1
            else:
                j += 1
        return max_child


            