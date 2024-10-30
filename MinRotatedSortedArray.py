class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        rotated = False
        min_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < min_num:
                rotated = True
                break
            
        
        if rotated:
            i = 0
            while (i<len(nums)-1):
                if nums[i] < nums[i+1]:
                    i += 1
                    continue
                else:
                    return nums[i+1]
        else:
            return nums[0]

        