class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        allTriplets = []
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            firstIndex = i + 1
            secondIndex = len(nums) - 1

            while firstIndex < secondIndex:
                if nums[firstIndex] + nums[secondIndex] + nums[i] > 0: #too high - second needs to be lower   
                    secondIndex -= 1        

                elif nums[firstIndex] + nums[secondIndex] + nums[i] < 0: #too low - second needs to be higher
                    firstIndex += 1

                elif nums[firstIndex] + nums[secondIndex] + nums[i] == 0:
                    triplet = [nums[i], nums[firstIndex], nums[secondIndex]]
                    allTriplets.append(triplet)
                    firstIndex += 1
                    secondIndex -= 1

                    while firstIndex < secondIndex and nums[firstIndex] == nums[firstIndex - 1]:
                        firstIndex += 1

        return allTriplets