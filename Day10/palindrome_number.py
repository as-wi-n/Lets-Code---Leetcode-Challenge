class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        word=x[::-1]
        if word==x:
            return True
        else:
            return False
        
        
