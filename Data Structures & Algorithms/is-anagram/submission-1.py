class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        if len(t)!=len(s):
            return False
        for index in range(0,len(s)):
            if s[index]!=t[index]:
                return False
        return True