class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum_digit=0
        num=x
        while num!=0:
            digit=num%10
            sum_digit+=digit
            num=num//10
        if (x%sum_digit)==0:
            return sum_digit
        else:
            return -1
        
