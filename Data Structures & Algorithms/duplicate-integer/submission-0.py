class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            value1 = nums[i]
            for j in range(len(nums)):
                if i != j and value1 == nums[j]:
                    return True
                
        return False