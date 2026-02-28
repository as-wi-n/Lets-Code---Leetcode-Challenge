class Solution(object):
    def defangIPaddr(self, address):
        result=""
        for ch in address:
            if ch==".":
                ch="[.]"
            result+=ch
        return result
      
