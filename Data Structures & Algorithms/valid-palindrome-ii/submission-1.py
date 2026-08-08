class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        add=0
        condition=False
        while right>left:
            if add==2:
                break
            if s[left]!=s[right]:
                right-=1
                add+=1
            else:
                left+=1
                right-=1
        if add<2:
            return True
        if condition==False:
            left,right=0,len(s)-1
            add=0
            while right>left:
                if add==2:
                    break
                if s[left]!=s[right]:
                    left+=1
                    add+=1
                else:
                    left+=1
                    right-=1
        if add<2:
            return True
        if condition==False:
            return False
        