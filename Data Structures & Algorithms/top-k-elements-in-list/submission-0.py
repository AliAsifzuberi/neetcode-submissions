class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashset = {}

        freqlist = []


        for num in nums:
            hashset[num] = hashset.get(num,0) + 1


        for num, count in hashset.items():
            freqlist.append((count,num))



        freqlist.sort()

        

        topk = freqlist[-k:]
        res = []
        for count, num in topk:
            res.append(num)
        return res