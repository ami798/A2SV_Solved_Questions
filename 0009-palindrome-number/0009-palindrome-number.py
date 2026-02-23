class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_number = str(x)  
        return str_number == str_number[::-1]  