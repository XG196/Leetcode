class Solution:

    def backtrack(self, start, nums, tmp, stoplevel):

        if len(tmp) == stoplevel:
            self.output.append(tmp[:])

        # do backtrack here
        for i in range(start, len(nums)):

            if i > 0 and nums[i] == nums[i-1] and i != start:
                continue

            tmp.append(nums[i])
            self.backtrack(i+1, nums, tmp, stoplevel)
            tmp.pop()

    def subsetsWithDup(self, nums: list[int]):

        nums.sort()
        self.output = [] 
        self.output.append([])
        self.n = len(nums)
        for stoplevel in range(self.n):
            self.backtrack(0, nums, [], stoplevel+1)
            
        return self.output
        