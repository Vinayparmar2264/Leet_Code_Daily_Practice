class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        print(ver1,ver2)
        i = 0
        while i < (min(len(ver1),len(ver2))):
            if int(ver1[i]) == int(ver2[i]):
                i+=1
                continue
            elif int(ver1[i]) >= int(ver2[i]):
                return 1
            else:
                return -1
            i +=1


        while i<len(ver1):
            if int(ver1[i])>0:
                return 1
            i += 1
        while i < len(ver2):
            if int(ver2[i])>0:
                return -1
            i += 1
        return 0
