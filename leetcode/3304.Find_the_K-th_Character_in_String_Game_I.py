class Solution:
    def kthCharacter(self, k: int) -> str:
        alphabet = [chr(c) for c in range(ord('a'), ord('z') + 1)]
        alphabet = "".join(alphabet)
        alphabet = alphabet + alphabet
        word = "a"

        while len(word) < k:
            new_word = ""
            for c in word:
                index = ord(c) - ord('a')
                new_word += alphabet[index + 1]
            word = word + new_word
        return word[k - 1]
