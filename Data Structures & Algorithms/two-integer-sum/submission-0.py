class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = 0
        output = []
        while x < len(nums):
            y = x+1
            while y < (len(nums)):
                res = nums[x] + nums[y]
                if res == target:

                    output.append(x)
                    output.append(y)

                    break

                else:

                    y+=1

            x+=1

        return output
