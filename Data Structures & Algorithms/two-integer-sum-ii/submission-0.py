class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        firstIndex = 0
        secondIndex = len(numbers) - 1

        while firstIndex < secondIndex:
            if numbers[firstIndex] + numbers[secondIndex] > target:
                secondIndex -= 1
            elif numbers[firstIndex] + numbers[secondIndex] < target:
                firstIndex += 1
            elif numbers[firstIndex] + numbers[secondIndex] == target:
                return [firstIndex + 1, secondIndex + 1]