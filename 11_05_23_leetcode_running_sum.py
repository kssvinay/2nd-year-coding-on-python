class Solution:
    def runningSum(self, arr: List[int]) -> List[int]:
        n=len(arr)
        pf=[0]*(n)
        pf[0]=arr[0]
        for i in range(1,n):
            pf[i]=pf[i-1]+arr[i]
        return pf
