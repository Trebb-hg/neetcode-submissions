class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist={number for number in nums}
        if len(exist)==len(nums):
            return False
        return True