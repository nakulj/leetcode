from collections import defaultdict
from functools import reduce


class WordDictionary:
    def __init__(self):
        self.words: dict[tuple[int, str, int], set[str]] = defaultdict(set)
        self.words_by_len:dict[int,set[str]] = defaultdict(set)

    def addWord(self, word: str) -> None:
        for i, c in enumerate(word):
            self.words[(i, c, len(word))].add(word)
        self.words_by_len[len(word)].add(word)

    def search(self, word: str) -> bool:
        if all(c == '.' for c in word):
            return len(self.words_by_len[len(word)]) > 0
        candidates = (
            self.words[i, c, len(word)]
            for i, c in enumerate(word)
            if c != "."
        )
        return len(reduce(lambda a, b: a & b, candidates)) > 0


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
