class Solution(object):
    def commonFactors(self, a, b):
        small=min(a,b)
        count=0
        for i in range(1,small+1):
            if a%i==0 and b%i==0:
                count+=1
        return count
        
