class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = [deck.pop()]
        for i in range(1, len(deck) + 1):
            res = [deck.pop()] + [res.pop()] + res
            
        return res