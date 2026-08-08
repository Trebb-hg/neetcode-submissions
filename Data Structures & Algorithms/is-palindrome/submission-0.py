class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1=[letter.lower() for letter in s if letter.isalnum()]
        return list1==list1[::-1]