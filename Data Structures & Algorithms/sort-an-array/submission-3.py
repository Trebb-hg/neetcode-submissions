class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def m(array,L,R):
            left,right=array[L:(L+(R-L)//2)+1],array[(L+(R-L)//2)+1:R+1]
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
                j+=1
                L+=1
            while k<len(right):
                array[L]=right[k]
                k+=1
                L+=1
            return array
        
        def ms(array,left,right):
            if left==right:
                return array
            ms(array,left,left+(right-left)//2)
            ms(array,(left+(right-left)//2)+1,right)
            m(array,left,right)
            return array

        return ms(nums,0,len(nums)-1)