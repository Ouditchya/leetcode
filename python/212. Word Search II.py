class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.cache_prefix = {}
        self.cache_search = {}
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True

    def prefix(self, word):
        if word in self.cache_prefix: return self.cache_prefix[word]
        node = self.root
        for c in word:
            if c not in node.children: 
                self.cache_prefix[word] = False
                return False
            node = node.children[c]
        self.cache_prefix[word] = True
        return True

    def search(self, word):
        if word in self.cache_search: return self.cache_search[word]
        node = self.root
        for c in word:
            if c not in node.children: 
                self.cache_search[word] = False
                return False
            node = node.children[c]
        self.cache_search[word] = node.is_end_of_word
        return node.is_end_of_word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        TrieAgain = Trie()
        for word in words: TrieAgain.insert(word)

        def solve(word, visited, r, c):
            nonlocal R, C, ans
            
            # Boundary condition
            if r < 0 or r >= R or c < 0 or c >= C: return
            
            # Already Visited?
            if visited[r][c] == 1: return

            # Make Choice
            visited[r][c] = 1
            word += board[r][c]
            # print(word)

            # If constructed word is not prefix in Trie, skip postprocessing
            if not TrieAgain.prefix(word): pass
            else:
                # If constructed word is a word in Trie, add to ans
                if TrieAgain.search(word): ans[word] = 1
                # Make Next Choices
                solve(word, visited, r, c+1)
                solve(word, visited, r, c-1)
                solve(word, visited, r-1, c)
                solve(word, visited, r+1, c)
            
            # Back Track
            visited[r][c] = 0
            word = word[0:len(word)-1]
    
        ans = {}
        R, C = len(board), len(board[0])
                 
        for r in range(R):
            for c in range(C):
                visited = [[0 for _ in range(C)] for _ in range(R)]
                solve('', visited, r, c) 

        return [x for x in ans.keys()]