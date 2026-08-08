class Solution:
    def scoreOfString(self, s: str) -> int:
        sum=0
        for index in range (1,len(s)):
            first=ord(s[index-1])
            second=ord(s[index])
            sum+=abs(first-second)
        return sum