class Solution(object):
    def returnToBoundaryCount(self, nums):
        n=len(nums)
        count=0
        move=0
        for i in range(0,n):
            move+=nums[i]
            if move==0:
                count+=1
        return count
