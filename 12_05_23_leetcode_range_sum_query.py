class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dic = {}
        self.dic[-1] = 0
        self.dic[0] = self.nums[0]
        for i in range(1,len(self.nums)):
            self.dic[i] = self.dic[i-1] + self.nums[i]
        #print(self.dic)
    def sumRange(self, left: int, right: int) -> int:
        return self.dic[right] - self.dic[left-1]
