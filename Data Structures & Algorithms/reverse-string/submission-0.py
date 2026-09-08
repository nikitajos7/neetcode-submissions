class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        front = 0
        end = len(s) - 1

        while front <= end:
            temp = s[front]
            s[front] = s[end]
            s[end] = temp
            front += 1
            end -= 1