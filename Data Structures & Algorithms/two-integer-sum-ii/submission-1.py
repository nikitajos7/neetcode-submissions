class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            index1 = numbers[start]
            index2 = numbers[end]
            if index1 + index2 == target:
                return [start + 1, end +1]
            elif index1 + index2 > target:
                end -= 1
            else:
                start += 1