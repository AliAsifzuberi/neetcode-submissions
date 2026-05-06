class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()


        for nums in nums:
            if nums in numset:
                return True
            else:
                numset.add(nums)
        

        return False
        