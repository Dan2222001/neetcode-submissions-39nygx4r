class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        highestCount = 1
        for num in nums:
            count = 1
            value = num
            if value - 1 not in nums:
                while True:
                    if value + 1 in nums:
                        count += 1
                        value += 1
                    else:
                        break
            if count > highestCount:
                highestCount = count
        return highestCount