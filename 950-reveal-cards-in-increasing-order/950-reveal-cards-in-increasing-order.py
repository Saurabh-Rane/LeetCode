class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = collections.deque([deck.pop()])
        for i in range(1, len(deck) + 1):
            queue.appendleft(queue.pop())
            queue.appendleft(deck.pop())
            
        return queue