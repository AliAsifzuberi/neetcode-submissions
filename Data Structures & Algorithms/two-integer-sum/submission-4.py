class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outputArr = []
        for x in range(len(nums)):
            for j in range(x+1,len(nums)):
                if nums[x] + nums[j] == target:
                    outputArr.append(x)
                    outputArr.append(j)
                    return outputArr
