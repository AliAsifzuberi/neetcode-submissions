class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxL = 0
        numbmer = {}

        for r in range(len(s)):
            numbmer[s[r]] = 1 + numbmer.get(s[r],0)

            while(r - left + 1) - max(numbmer.values()) > k:
                numbmer[s[left]] -=1
                left+=1
            
            maxL = max(maxL,r - left + 1)

        return maxL
            