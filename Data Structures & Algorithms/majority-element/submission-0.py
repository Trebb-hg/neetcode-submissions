class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        for number in nums:
            if number not in dict:
                dict[number]=1
            else:
                dict[number]+=1
        maxi=-1
        keyers=''
        for key in dict:
            if dict[key]>maxi:
                maxi=max(dict[key],maxi)
                keyers=key
        return keyers
