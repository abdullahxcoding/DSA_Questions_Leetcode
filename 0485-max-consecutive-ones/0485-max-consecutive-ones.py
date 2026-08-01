class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0 
        ones = 0
        for i in range(0,len(nums)):
            if nums[i] == 1 :
                ones=ones+1 
            else :
                ones = 0 
            max_ones = max(ones,max_ones)
        return max_ones

        