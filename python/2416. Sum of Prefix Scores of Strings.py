class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.cnt_visit = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode()
            node.cnt_visit[c] = node.cnt_visit.get(c, 0) + 1
            node = node.children[c]
        node.is_end_of_word = True

    def prefix(self, word):
        node = self.root
        cnt = 0
        for c in word:
            if c not in node.children: return cnt
            cnt += node.cnt_visit[c]
            # print("node: ", c, " node.cnt_visit: ", node.cnt_visit, " cnt: ", cnt)
            node = node.children[c]
        #     print(c, ": ", node.cnt_visit, " cnt: ", cnt)
        # print("-----------------------------------")
        return cnt

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        TriedSoHardAndGotSoFar = Trie()

        for word in words: TriedSoHardAndGotSoFar.insert(word)

        ans = []
        for word in words: ans.append(TriedSoHardAndGotSoFar.prefix(word))

        return ans