class Solution:
    def passwordStrength(self, password: str) -> int:
        password = set(password)
        s = 0

        for ch in password:
            if ch.isalpha():
                if ch.islower():
                    s += 1
                else:
                    s += 2

            elif ch.isdigit():
                s += 3

            else:
                s += 5
                
        return s

        