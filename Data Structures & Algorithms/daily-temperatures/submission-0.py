class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexes = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while indexes and temperatures[indexes[-1]] < t:
                prev = indexes.pop()
                result[prev] = i - prev
            indexes.append(i)

        return result