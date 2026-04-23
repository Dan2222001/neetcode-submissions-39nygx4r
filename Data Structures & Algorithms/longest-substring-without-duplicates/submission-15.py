class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        used = {}
        longest, l, r = 0, 0, 0
        for i, c in enumerate(s):
            r += 1
            if used.get(c) is None:
                used[c] = i
            else:
                if used.get(c) + 1 > l:
                    l = used.get(c) + 1
                used[c] = i
            longest = max(longest, r - l)      
        
        longest = max(longest, r - l)
        return longest