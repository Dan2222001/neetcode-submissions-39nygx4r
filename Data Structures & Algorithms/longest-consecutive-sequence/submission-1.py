class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        highestCount = 1
        numSet = set(nums)
        for num in nums:
            count = 1
            if num - 1 not in nums:
                while True:
                    if num + 1 in nums:
                        count += 1
                        num += 1
                    else:
                        break

            if count > highestCount:
                highestCount = count
        
        return highestCount