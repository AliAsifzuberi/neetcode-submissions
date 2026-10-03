class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        left = 0
        maxSub = 0

        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[left])
                left+=1
            
            substring.add(s[r])
            maxSub = max(maxSub, r-left+1)

        return maxSub