class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        suffix = [0] * (len(nums) + 1)
        prefix[0] = 0
        suffix[len(nums)] = 0

        prefix[1] = nums[0]
        suffix[len(nums) -1] = nums[len(nums) - 1]

        nums.insert(0, 0)
        nums.insert(len(nums), 0)

        for i in range(2, len(nums)-1):
            prefix[i] = nums[i] + prefix[i - 1]

        for i in range(len(nums) - 3, -1, -1):
            suffix[i] = nums[i + 1] + suffix[i + 1]


        print(prefix)
        print(suffix)

        for i in range(1, len(nums) - 1):
            if prefix[i - 1] == suffix[i]:
                return i - 1

        return -1
        








