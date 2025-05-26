class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for c in word:
                if c not in node.children: node.children[c] = TrieNode()
                node = node.children[c]
            node.is_end_of_word = True

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        for i in range(n):
            if i == 0: wildcardWord = '.' + searchWord[i+1:]
            elif i == n-1: wildcardWord = searchWord[:n-1] + '.'
            else: wildcardWord = searchWord[:i] + '.' + searchWord[i+1:]
            x = searchWord[i]
            # print(wildcardWord)
            if self.dfs_search(self.root, wildcardWord, x): return True
        return False

    def dfs_search(self, node, searchWord, x) -> bool:
        n = len(searchWord)

        for i in range(n):

            flag_continue = False

            if searchWord[i] == '.':
                if i == n-1:
                    for c in node.children:
                        if c == x: continue
                        curr = node.children[c]
                        if curr.is_end_of_word: return True
                    return False
                else:
                    check = False
                    for c in node.children:
                        if c == x: continue
                        curr = node.children[c]
                        check = self.dfs_search(curr, searchWord[i+1:], x)
                        if check: break
                    if check: node, flag_continue = curr, True
                    else: return False

                if flag_continue: continue

            elif searchWord[i] not in node.children: return False

            node = node.children[searchWord[i]]
        
        return node.is_end_of_word


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)