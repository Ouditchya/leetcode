class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        return self.dfs_search(self.root, word)

    def dfs_search(self, node, word):
        wordLen = len(word)

        for i in range(wordLen):
            
            flag_continue = False

            if word[i] == '.':
                if i == wordLen-1:
                    for x in node.children:
                        curr = node.children[x]
                        if curr.is_end_of_word: return True
                    return False
                else:
                    check = False
                    for x in node.children: 
                        curr = node.children[x]
                        check = self.dfs_search(node.children[x], word[i+1:])
                        if check: break
                    if check: node, flag_continue = curr, True
                    else: return False

                if flag_continue: continue
            
            elif word[i] not in node.children:
                return False
            
            node = node.children[word[i]]
        
        return node.is_end_of_word

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)