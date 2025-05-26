class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True

    def isprefix(self, word):
        node = self.root
        prefix = ''
        for c in word:
            if c not in node.children: return word
            prefix += c
            node = node.children[c]
            if node.is_end_of_word: return prefix
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        TrieAgain = Trie()
        for word in dictionary: TrieAgain.insert(word)

        sentenceList = sentence.split()
        nWords = len(sentenceList)
        for i in range(nWords): sentenceList[i] = TrieAgain.isprefix(sentenceList[i])

        return ' '.join(x for x in sentenceList)