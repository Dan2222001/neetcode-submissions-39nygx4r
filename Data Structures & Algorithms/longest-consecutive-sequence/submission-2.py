class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        highestCount = 1
        numSet = set(nums)
        for num in numSet:
            count = 1
            if num - 1 not in numSet:
                while True:
                    if num + 1 in numSet:
                        count += 1
                        num += 1
                    else:
                        break

            if count > highestCount:
                highestCount = count
        
        return highestCount