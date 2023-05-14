class Solution:
    def subarraySum(self, nums, k) :
        c=0
        n=len(nums)
        pfsum=0
        d={0:1}
        for i in range(0,n):
            pfsum=pfsum+nums[i]
            if pfsum-k in d:
                c=c+d[pfsum-k]
            if pfsum not in d:
                d[pfsum]=1
            else:
                d[pfsum]=d[pfsum]+1
        return c
