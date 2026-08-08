class Solution:
    def countSeniors(self, details: List[str]) -> int:
        sum=0
        for detail in details:
            strink=""
            for index in range(11,13):
                strink+=detail[index]
            if int(strink)>60:
                sum+=1
        return sum