class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        answ=0
        d={}
        for x in nums:
            if x in d: d[x]+=1
            else:      d[x]=1
        
        if k:
            answ=sum(x+k in d for x in d.keys())
        else:
            answ=sum(k>1 for k in d.values())
                
        return answ
