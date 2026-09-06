class Solution:
    def isValid(self, s: str) -> bool:
        open = "([{"
        close = ")]}"
        close = {")":"(", "]":"[","}":"{"}

        stack = []

        for i in range(len(s)):

            if s[i] in open:
                stack.append(s[i])
                 
            elif stack and s[i] in close:
                if stack[-1] == close[s[i]]:
                    stack.pop()
                    
                else:
                    return False

            else:
                return False
        
        if stack:
            return False
        return True