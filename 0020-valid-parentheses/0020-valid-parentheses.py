class Solution:
    def isValid(self, s: str) -> bool:
        open = "([{"
        close = ")]}"

        stack = []

        for i in range(len(s)):

            if s[i] in open:
                stack.append(s[i])
                 
            elif stack and s[i] in close:
                if s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                elif s[i] == "]" and stack[-1] == "[" :
                    stack.pop()
                elif s[i] == "}" and stack[-1] == "{" :
                    stack.pop()
                else:
                    return False

            else:
                return False
        
        if stack:
            return False
        return True