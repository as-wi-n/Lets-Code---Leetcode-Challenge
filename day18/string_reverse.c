class Solution(object):
    def reverseWords(self, s):
        result=[]
        word=""
        for ch in s:
            if ch!=" ":
                word+=ch
            else:
                result.append(word[::-1])
                result.append(" ")
                word=""
        result.append(word[::-1])
        return "".join(result)

            
