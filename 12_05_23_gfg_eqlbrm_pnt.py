class Solution:
    def equilibriumPoint(self,A, N):
        lsum = 0
        rsum = sum(A)
        for i in range(N):
            rsum -= A[i]
            if lsum == rsum:
                return i+1
            lsum += A[i]
        return -1
        # Your code here
