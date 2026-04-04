class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        result1=''.join(word1)
        result2=''.join(word2)
        if result1==result2:
            return True
        else:
            return False
        
