class Solution:
    def reverseWords(self, s: str) -> str:
        lst = []
        lst1 = list(s.strip().split(" "))
        for i in range(len(lst1)-1,-1,-1):
            if lst1[i]!='':
                lst.append(lst1[i])
        print(lst)
        s = " ".join(lst)
        return s
