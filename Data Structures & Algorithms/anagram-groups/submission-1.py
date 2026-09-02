class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            sort = str(sorted(word))
            if sort in hashmap:
                hashmap[sort].append(word)
            else:
                hashmap[sort] = [word]

        result = []

        for groups in hashmap:
            result.append(hashmap[groups])

        return(result)