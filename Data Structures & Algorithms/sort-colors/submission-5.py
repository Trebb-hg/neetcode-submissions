class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right=0,len(nums)-1
        i=0
        while i<=right:
            if nums[i]==0:
                temp=nums[left]
                nums[left]=nums[i]
                nums[i]=temp
                left+=1
            elif nums[i]==2:
                temp=nums[right]
                nums[right]=nums[i]
                nums[i]=temp
                right-=1
                i-=1
            i+=1
        