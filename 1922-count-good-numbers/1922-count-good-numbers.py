class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def mod_pow(base, exp):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return result

        evens = (n + 1) // 2   
        odds = n // 2        
        
        return (mod_pow(5, evens) * mod_pow(4, odds)) % MOD

            
                
                
                    
                

        
