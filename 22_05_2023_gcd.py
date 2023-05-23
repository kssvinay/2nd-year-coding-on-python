class Solution:
    def gcd(self, A, B):
        if A==0:
            return B
        return self.gcd(B%A,A)
