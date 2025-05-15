from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort(reverse = True)
        dq = deque()
        dq.append(deck[0])

        for i in range(1, n):
            curr = dq.pop()
            dq.appendleft(curr)
            dq.appendleft(deck[i])

        return [x for x in dq]