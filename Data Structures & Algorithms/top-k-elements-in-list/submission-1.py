class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numhash = {}

        for num in nums:
            if num in numhash:
                numhash[num] +=1
            else:
                numhash[num] = 1

        bucks = []

        for _ in range(len(nums)+1):
            bucks.append([])
        
        for num, count in numhash.items():
            bucks[count].append(num)

        res = []

        for i in range(len(bucks)-1,0,-1):
            for nums in bucks[i]:
                res.append(nums)
                if len(res) == k:
                    return res