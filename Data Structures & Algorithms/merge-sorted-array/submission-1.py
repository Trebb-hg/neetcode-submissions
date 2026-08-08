class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        list_index=len(nums1)-1
        indexn=n-1
        indexm=m-1
        while indexn>-1:
            if indexm>=0 and nums1[indexm]>nums2[indexn]:
                nums1[list_index]=nums1[indexm]
                indexm-=1
            else:
                nums1[list_index]=nums2[indexn]
                indexn-=1
            list_index-=1
