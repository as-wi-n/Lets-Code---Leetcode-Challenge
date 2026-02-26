class Solution(object):
    def averageValue(self, nums):
        n=len(nums)
        count=0
        total=0
        for i in range(0,n):
            if nums[i]%2==0 and nums[i]%3==0:
                total+=nums[i]
                count+=1
        if count==0:
            return 0
        else:
            return total//count
        
