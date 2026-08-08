class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for index in range(0,2*len(nums)):
            ans.append(nums[index%n])
        return ans