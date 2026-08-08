class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        index1,sum=1,0
        for index in range(1,len(nums)):
            if nums[index]!=nums[index-1]:
                nums[index1]=nums[index]
                index1+=1
        return index1
