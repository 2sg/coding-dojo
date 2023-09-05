class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        
        # Initialize the result array with 1s
        res = [1] * n
        
        # Compute left products
        # For each nums[i], res[i] contains the product of all elements on the left
        left_product = 1
        for i in range(1, n):
            left_product *= nums[i - 1]
            res[i] *= left_product
        
        # Compute right products
        # For each nums[i], multiply res[i] with the product of all elements on the right
        right_product = 1
        for i in reversed(range(n - 1)):
            right_product *= nums[i + 1]
            res[i] *= right_product
        
        return res