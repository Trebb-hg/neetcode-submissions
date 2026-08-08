class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        res=set(nums)
        nums[:]=res
        nums.sort()
        return len(nums)