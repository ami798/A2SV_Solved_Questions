class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x,-n)
        hf = self.myPow(x , n // 2 )

        if n % 2 == 0:
            return hf * hf
        else:
            return x*hf*hf 

            