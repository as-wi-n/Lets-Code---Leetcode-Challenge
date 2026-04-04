class Solution(object):
    def restoreString(self, s, indices):
        n=len(indices)
        word=['']*n
        for i in range(0,n):
            word[indices[i]]=s[i]
        return ''.join(word)
        
