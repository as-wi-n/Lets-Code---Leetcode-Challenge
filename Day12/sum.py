class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        digit_sum=0
        n=len(nums)
        for i in range(0,n):
            total+=nums[i]
            while(nums[i]!=0):
                digit=nums[i]%10
                digit_sum+=digit
                nums[i]=nums[i]/10
        return abs(total-digit_sum)

        
