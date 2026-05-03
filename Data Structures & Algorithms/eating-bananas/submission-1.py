import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        minValue = r
        

        while l <= r:
            time = h
            mid = (l + r) // 2

            for i in piles:
                time -= math.ceil(i / mid)
                if time < 0:
                    break
            
            if time < 0:
                l = mid + 1
            else:
                minValue = min(minValue, mid)
                r = mid - 1

        return minValue