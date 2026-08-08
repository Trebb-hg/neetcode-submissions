class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sum,current=0,-10000000
        res=[]
        for index in range(0,len(nums)):
            if nums[index]>current:
                current=nums[index]
                sum+=1
                res.append(nums[index])
        nums[:]=res
        return sum