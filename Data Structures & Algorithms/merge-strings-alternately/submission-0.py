class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1,length2=len(word1),len(word2)
        max_length=max(length1,length2)
        index1,index2=0,0
        res=""
        while index1<length1 or index2<length2:
            if index1>=length1:
                res+=word2[index2]
                index2+=1
            elif index2>=length2:
                res+=word1[index1]
                index1+=1
            else:
                res+=word1[index1]
                res+=word2[index2]
                index1+=1
                index2+=1
        return res