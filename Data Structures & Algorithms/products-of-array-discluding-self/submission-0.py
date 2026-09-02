class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        prefix=1
        for i in range(0,len(nums)):
            res.append(prefix)
            prefix*=nums[i]
        backfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=backfix*res[i]
            backfix*=nums[i]
        return res