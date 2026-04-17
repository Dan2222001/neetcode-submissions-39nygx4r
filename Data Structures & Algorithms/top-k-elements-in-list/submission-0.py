class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        to_ret = []
        for int in nums:
            if int not in frequencies:
                frequencies[int] = 1
            else:
                frequencies[int] += 1

        for i in range(k):
            highest_key = max(frequencies, key=frequencies.get)
            to_ret.append(highest_key)
            del frequencies[highest_key]
        return to_ret