class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prefix=1
        for i in range(0,len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        prefix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=prefix * res[i]
            prefix*=nums[i]
        return res