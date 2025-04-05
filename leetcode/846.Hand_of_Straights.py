#IDEA: Counter + Sort by value of card
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        counter = sorted([[k, v] for k, v in counter.items()], key=lambda x: x[0])
        n = len(counter)
        
        for i in range(n):
            if counter[i][1] != 0:
                if n - i < groupSize:
                    return False
                k = counter[i][1]
                for j in range(i, i + groupSize):
                    if counter[j][0] != counter[i][0] + j - i:
                        return False
                for j in range(i, i + groupSize):
                    counter[j][1] -= k
                    if counter[j][1] < 0:
                        return False
        return True
