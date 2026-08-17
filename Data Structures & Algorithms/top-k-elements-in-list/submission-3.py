class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction={}
        lis=[[] for i in range(len(nums)+1)]
        for number in nums:
            diction[number]=1+diction.get(number,0)
        for key,value in diction.items():
            lis[value].append(key)
        res=[]
        for i in range(len(lis)-1,0,-1):
            for number in lis[i]:
                res.append(number)
                if len(res)==k:
                    return res