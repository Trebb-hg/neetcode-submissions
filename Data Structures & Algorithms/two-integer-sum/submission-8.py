class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for index in range(0,len(nums)):
            if target-nums[index] not in dict:
                dict[nums[index]]=index
            else:
                return [dict[target-nums[index]],index]