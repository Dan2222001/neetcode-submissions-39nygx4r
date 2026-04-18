class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        for i in range(len(nums)):
            prefix = 1
            suffix = 1
            for k in nums[:i]:
                prefix *= k

            for k in nums[i+1:]:
                suffix *= k

            products.append(prefix * suffix)
        
        return products