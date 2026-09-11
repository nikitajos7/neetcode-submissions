class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxCount = 0

        for num in hashset:
            if num - 1 not in hashset:
                curr = num
                count = 1

                while curr + 1 in hashset:
                    curr += 1
                    count += 1

                maxCount = max(maxCount, count)

        return maxCount
