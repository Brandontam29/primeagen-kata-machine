from typing import Optional


class Node:
    def __init__(self, c: str, is_word: bool):
        self.letter = c
        self.is_word = is_word
        self.children: list[Node] = [None for _ in range(26)]


class TrieAutocomplete:
    def __init__(self):
        self.children: list[Node] = [None for _ in range(26)]

    def addWord(self, word: str):
        letters = list(word)

        curr = self.children
        for i, c in enumerate(letters):
            is_word = i == len(letters) - 1
            index: int = self._char_to_index(c)

            if curr[index]:
                if is_word:
                    curr[index].is_word = True
                curr = curr[index].children
                continue

            node = Node(c, is_word)

            curr[index] = node
            curr = node.children

    def _walk(self, curr: Optional["Node"], path: list[str], words: list[str]):
        if not curr:
            return
        path.append(curr.letter)
        if curr.is_word:
            words.append("".join(path))

        for node in curr.children:
            self._walk(node, path, words)

        path.pop()

        return

    def get_all_words(self):
        words: list[str] = []
        path: list[str] = []

        for node in self.children:
            self._walk(node, path, words)

        return words

    def autocomplete(self, s: str):
        words: list[str] = []
        path: list[str] = list(s)
        letters = list(s)

        curr = self.children

        for c in letters:
            index: int = self._char_to_index(c)

            if curr[index]:
                curr = curr[index].children
                continue

            return words

        for node in curr:
            self._walk(node, path, words)

        return words

    def _char_to_index(self, c: str) -> int:
        return ord(c) - ord("a")


trie = TrieAutocomplete()

trie.addWord("cat")
trie.addWord("cattle")
trie.addWord("cup")
trie.addWord("can")
trie.addWord("bear")
trie.addWord("bee")
trie.addWord("bill")
trie.addWord("billy")
trie.addWord("cats")
trie.addWord("zebra")
trie.addWord("zeal")
trie.addWord("zigzag")
trie.addWord("meal")
trie.addWord("man")
trie.addWord("men")
trie.addWord("menace")
trie.addWord("meaning")
trie.addWord("merely")
trie.addWord("manifestation")
trie.addWord("manifest")
trie.addWord("maniac")
print(trie.get_all_words())
print(trie.autocomplete("ma"))
