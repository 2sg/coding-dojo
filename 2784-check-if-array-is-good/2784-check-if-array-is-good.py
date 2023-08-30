class Solution:
    def isGood(self, nums):
        n = max(nums)
        return nums.count(n) == 2 and len(nums) == n + 1 and len(set(nums)) == n
