class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            seq = "".join(sorted(word))

            hashmap.setdefault(seq, []).append(word)

        return list(hashmap.values())