from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        unique_chars = set(word1)
        unique_chars_word2 = set(word2)
        if unique_chars != unique_chars_word2:
            return False
        cnt_word1 = list(Counter(word1).values())
        cnt_word2 = list(Counter(word2).values())
        cnt_word1.sort()
        cnt_word2.sort()
        return cnt_word1 == cnt_word2

