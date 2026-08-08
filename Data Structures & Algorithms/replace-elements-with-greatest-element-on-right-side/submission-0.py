class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_largest=-1
        for index in range(len(arr)-1,-1,-1):
            temp=arr[index]
            arr[index]=current_largest
            current_largest=max(current_largest,temp)
        return arr