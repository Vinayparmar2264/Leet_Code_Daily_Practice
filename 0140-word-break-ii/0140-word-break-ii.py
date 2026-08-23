class Solution:
    def solve(self,idx,s,wordDict,path,result):
        if idx >= len(s):
            result.append(" ".join(path))

        for i in range(idx,len(s)):
            if s[idx:i+1] in wordDict:
                path.append(s[idx:i+1])
                self.solve(i+1,s,wordDict,path,result)
                path.pop()




    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        result = []
        self.solve(0,s,wordDict,[],result)
        return result