class Solution:

    def find_subsets(self, nums, res, i, tmp, stop_level):

        # append to res
        if len(tmp) == stop_level:
            res.append(tmp[:])
            return
        
        # at recursive level
        while (i < len(nums)):
            tmp.append(nums[i])
            self.find_subsets(nums, res, i+1, tmp, stop_level)
            tmp.pop()
            i += 1


    def subsets(self, nums: list[int]):

        # backtrack to search power sets at per stoplevel
        # handle the stoplevel using a loop
        res = []
        tmp = []
        res.append(tmp[:])  # empty set
        stop_level = 1   # recursive level

        i = 0
        for stop_level in range(1, len(nums)+1):
            self.find_subsets(nums, res, i, tmp, stop_level) 

        return res



