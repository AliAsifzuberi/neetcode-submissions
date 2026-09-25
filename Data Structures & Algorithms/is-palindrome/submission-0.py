class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring = ""
        for char in s:
            if char.isalnum() == True:
                newstring = newstring + char.lower()

        left = 0
        right = len(newstring) - 1

        while(left<=right):
            if newstring[left] == newstring[right]:
                left+=1
                right-=1
            elif newstring[left] != newstring[right]:
                return False
        return True
        

        
        

        