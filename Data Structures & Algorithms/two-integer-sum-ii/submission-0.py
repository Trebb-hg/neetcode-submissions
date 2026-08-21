class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        one,two=0,len(numbers)-1
        while two>one:
            if numbers[one]+numbers[two]<target:
                one+=1
            elif numbers[one]+numbers[two]>target:
                two-=1
            else:
                break
        res=[]
        res.append(one+1)
        res.append(two+1)
        return res
        