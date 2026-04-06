class Solution(object):
    def findFinalValue(self, nums, original):
        n=len(nums)
        while original in nums:
                original=original*2
        return original
        
