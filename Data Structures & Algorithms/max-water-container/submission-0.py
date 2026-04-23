class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        l, r = 0, len(heights) - 1

        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            if curr > max:
                max = curr

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max