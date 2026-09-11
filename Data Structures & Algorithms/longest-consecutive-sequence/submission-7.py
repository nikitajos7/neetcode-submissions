class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()

        count = 1
        maxCount = 1
        index = 0

        while index < len(nums) - 1:
            count = 1
            index += 1

            while index < len(nums) and (nums[index] == nums[index - 1] + 1 or nums[index] == nums[index - 1]):
                if nums[index] == nums[index - 1] + 1:
                    count += 1
                index += 1

            maxCount = max(count, maxCount)
            
        return maxCount