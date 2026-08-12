class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency=[[] for i in range(len(nums)+1)]
        count={}
        for number in nums:
            count[number]=1+count.get(number,0)
        for number,coun in count.items():
            frequency[coun].append(number)
        res=[]
        for i in range(len(frequency)-1,0,-1):
            for number in frequency[i]:
                res.append(number)
                if len(res)==k:
                    return res
