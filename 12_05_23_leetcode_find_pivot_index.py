class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = [0]*len(nums)
        rsum = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                lsum[i] = 0
                rsum[i] = sum(nums[1:])
            else:
                lsum[i] = lsum[i-1] + nums[i-1]
                rsum[i] = rsum[i-1] - nums[i]
            if lsum[i] == rsum[i]:
                return i
        return -1
