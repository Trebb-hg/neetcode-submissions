class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(array,L,M,R):
            left,right=array[L:M+1],array[M+1:R+1]
            j,k=0,0
            while j<len(left) and k<len(right):
                if left[j]<=right[k]:
                    array[L]=left[j]
                    j+=1
                else:
                    array[L]=right[k]
                    k+=1
                L+=1
            while j<len(left):
                array[L]=left[j]
                L+=1
                j+=1
            while k<len(right):
                array[L]=right[k]
                L+=1
                k+=1
            return array

        
        def mergesort(array,left,right):
            if left==right:
                return array
            mergesort(array,left,left+(right-left)//2)
            mergesort(array,left+(right-left)//2+1,right)
            merge(array,left,left+(right-left)//2,right)
            return array
        return mergesort(nums,0,len(nums)-1)
