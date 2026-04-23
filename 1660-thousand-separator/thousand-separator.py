class Solution(object):
    def thousandSeparator(self, n):
        s = str(n)
        result = ""
        
        while len(s) > 3:
            result = "." + s[-3:] + result
            s = s[:-3]
        
        return s + result
