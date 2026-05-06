class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordset = {}


        for words in strs:
            key = "".join(sorted(words))
            
            if key in wordset:
                wordset[key].append(words)
            else:
                wordset[key] = [words]
        return list(wordset.values()
        )