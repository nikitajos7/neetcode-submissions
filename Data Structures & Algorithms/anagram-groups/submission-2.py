class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            key = str(sorted(word))

            hashmap.setdefault(key, []).append(word)

        result = []

        for key in hashmap:
            result.append(hashmap[key])

        return result