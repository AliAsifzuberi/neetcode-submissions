class Solution:

    def encode(self, strs: List[str]) -> str:
        ress = ""
        for s in strs:
            ress = ress + str(len(s))+"#"+s
        return ress 


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i  
            while s[j] != "#":
                j += 1
            lens = int(s[i:j])
            res.append(s[j+1 : j+1+lens])
            i = j + 1 + lens

        return res  
