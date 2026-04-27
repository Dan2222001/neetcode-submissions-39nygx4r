class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permChars = [0] * 26
        curChars = [0] * 26
        for c in s1:
            permChars[ord(c) - ord('a')] += 1

        l, r = 0, len(s1) - 1

        for i, c in enumerate(s2):
            if i == len(s1):
                break
            else:
                curChars[ord(c) - ord('a')] += 1


        if permChars == curChars:
            return True

        while r < len(s2) - 1:
            curChars[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            curChars[ord(s2[r]) - ord('a')] += 1

            if permChars == curChars:
                return True
            
        return False