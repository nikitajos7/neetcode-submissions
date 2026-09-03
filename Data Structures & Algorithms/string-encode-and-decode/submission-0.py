class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""

        for i in range(len(strs)):
            word = list(strs[i])
            for j in range(len(word)):
                word[j] = chr(ord(word[j]) + 5)

            encoded_string += "".join(word)
            encoded_string += " "

        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        word = []
        for i in range(len(s)):

            if ord(s[i]) == 32:
                decoded_strs.append("".join(word))
                word = []
            else:
                word.append(chr(ord(s[i]) - 5))

        return decoded_strs
        