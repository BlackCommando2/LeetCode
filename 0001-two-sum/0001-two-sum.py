class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        if(len(nums)==2):
            return [0,1]
        for i in range(len(nums)):
            compliment = target-nums[i]
            if compliment in dict:
                return [dict[compliment],i]
            dict[nums[i]] = i     