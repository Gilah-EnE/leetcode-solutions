from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_counter = Counter(text)
        b = text_counter["b"]
        a = text_counter["a"]
        l = text_counter["l"] // 2
        o = text_counter["o"] // 2
        n = text_counter["n"]

        return min(b, a, l, o, n)
