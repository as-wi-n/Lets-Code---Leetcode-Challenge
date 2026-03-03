class Solution(object):
    def twoSum(self, nums, target):
        length=len(nums)
        for i in range(0,length):
            n=nums[i]
            for j in range(i+1,length):
                if n+nums[j]==target:
                    return [i,j]
