class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tList = list(t)
        for i in s:
            if len(tList) == 0:
                return False
            
            if i in tList:
                tList.remove(i)

        if tList == []:
            return True
        else:
            return False