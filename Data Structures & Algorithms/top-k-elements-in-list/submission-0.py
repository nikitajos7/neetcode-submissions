class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        counts = list(hashmap.values())
        counts.sort(reverse=True)
        counts = counts[:k]

        result = []

        for key in hashmap:
            if hashmap[key] in counts:
                result.append(key)

        return result  




