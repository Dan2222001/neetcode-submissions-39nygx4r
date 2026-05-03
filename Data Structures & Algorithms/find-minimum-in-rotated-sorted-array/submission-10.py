class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[l] <= nums[mid] and nums[mid] <= nums[r]:
                return nums[l]
            elif nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid