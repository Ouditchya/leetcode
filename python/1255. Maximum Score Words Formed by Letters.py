class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        hashLetters = {}
        for x in letters: hashLetters[x] = hashLetters.get(x, 0) + 1
        # print(hashLetters)

        hashWords = {}
        for word in words:
            val = 0
            for c in word: val += score[ord(c)-97]
            hashWords[word] = val
        # print(hashWords)

        def check(word, hashLetters):
            for c in word:
                if hashLetters.get(c, 0) == 0: return False
                hashLetters[c] -= 1
            return True

        def updateSelect(word, hashLetters):
            for c in word: hashLetters[c] -= 1
            return hashLetters

        def updateBacktrack(word, hashLetters):
            for c in word: hashLetters[c] += 1
            return hashLetters

        def solve(idx, selectScore, hashLetters):
            nonlocal nWords, maxScore, debug

            # All Possible Choices
            for i in range(idx, nWords):  
                # If Choice can be made  
                if check(words[i], hashLetters.copy()):
                    # Make Choice
                    hashLetters = updateSelect(words[i], hashLetters.copy())
                    selectScore += hashWords[words[i]]
                    maxScore = max(maxScore, selectScore)
                    
                    if debug:
                        print("Selected: ", words[i], " Current Score: ", selectScore, " Max Score: ", maxScore)
                        print("Updated hash: ", hashLetters)
                    
                    # Explore Other Choices
                    solve(i+1, selectScore, hashLetters.copy())
                    
                    # Backtrack Current Choice
                    hashLetters = updateBacktrack(words[i], hashLetters.copy())
                    selectScore -= hashWords[words[i]]

                    if debug:
                        print("Backtracked: ", words[i], " Current Score: ", selectScore, " Max Score: ", maxScore)
                        print("Updated hash: ", hashLetters, "\n----------------------------------------")

        nWords = len(words)
        maxScore = 0
        debug = False
        solve(0, 0, hashLetters.copy())

        return maxScore
