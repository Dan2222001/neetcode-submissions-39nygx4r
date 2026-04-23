class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        allTriplets = []
        nums.sort()
        for i in range(len(nums)):
            firstIndex = 0
            secondIndex = len(nums) - 1
            if i == firstIndex:
                firstIndex += 1
            elif i == secondIndex:
                secondIndex -= 1

            while firstIndex < secondIndex:
                if nums[firstIndex] + nums[secondIndex] + nums[i] == 0:
                    triplet = [nums[firstIndex], nums[secondIndex], nums[i]]
                    triplet.sort()
                    if triplet not in allTriplets:
                        allTriplets.append(triplet)
                    firstIndex += 1
                    if firstIndex == i:
                        firstIndex += 1
                
                elif nums[firstIndex] + nums[secondIndex] + nums[i] > 0: #too high - second needs to be lower
                    secondIndex -= 1
                    if secondIndex == i:
                        secondIndex -= 1
                
                elif nums[firstIndex] + nums[secondIndex] + nums[i] < 0: #too low - second needs to be higher
                    firstIndex += 1
                    if firstIndex == i:
                        firstIndex += 1

        return allTriplets