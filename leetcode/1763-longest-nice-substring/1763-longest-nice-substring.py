class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(string):
            if len(string) < 2:
                return ""
            set_s =  set(string)
            for i,c in enumerate(string):
                if c.swapcase() not in set_s:
                    left = helper(string[:i])
                    right = helper(string[i+1:])
                    return right if len(right) > len(left) else left
            return string
                
        return helper(s)
                    

