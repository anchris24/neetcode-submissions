class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        freq = Counter(hand)
        for num in hand:
            start = num
            if not freq[num]:
                continue

            while freq[start - 1]:
                start -= 1
            
            for i in range(start, start + groupSize):
                if not freq[i]:
                    return False
                freq[i] -= 1
        return True
            
