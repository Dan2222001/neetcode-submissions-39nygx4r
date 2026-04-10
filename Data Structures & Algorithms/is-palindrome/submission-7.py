class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2 and p1 < len(s) and p2 >= 0:
            while p1 < len(s) and not s[p1].isalnum():
                p1 += 1
            while p2 >= 0 and not s[p2].isalnum():
                p2 -= 1
            if p1 >= p2 or p1 > len(s) + 1 or p2 < 0:
                break
            if s[p1].lower() != s[p2].lower():
                return False
            else:
                p1 += 1
                p2 -= 1
            
        return True