class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        for i in range(1,num+1):
            n=i
            digit_sum=0
            while(n!=0):
                digit=n%10
                digit_sum+=digit
                n=n/10
            if digit_sum%2==0:
                count+=1
        return count
