class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:

        new_word: list = []
        min_word_length: int = min(len(word1), len(word2))

        for i in range(0, min_word_length):
            new_word.append(word1[i])
            new_word.append(word2[i])

        for j in range(min_word_length, len(word1)):
            new_word.append(word1[j])

        for k in range(min_word_length, len(word2)):
            new_word.append(word2[k])

        return "".join(new_word)