class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        sum=0
        useless=[]
        returned_list=[]
        for index in range(0,len(nums)):
            if nums[index]!=val:
                returned_list.append(nums[index])
                sum+=1
            else:
                useless.append(nums[index])
        nums[:]=returned_list + useless
        return sum