class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0  # Starts at 0 in case nums is empty

        for num in num_set:
            # Check if this num is the start of a train
            if (num - 1) not in num_set:
                curr = num
                length = 1  # A single number is a sequence of length 1

                while (curr + 1) in num_set:
                    curr += 1
                    length += 1

                longest = max(longest, length)

        return longest