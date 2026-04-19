class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counter = [0] * 1000
        for num in hand:
            counter[num] += 1

        total = sum(counter)
        for i in range(len(counter)):
            if counter[i] != 0:
                needed = counter[i]
                counter[i] -= needed
                for j in range(i + 1, i + groupSize):
                    counter[j] -= needed
                    if counter[j] < 0:
                        return False
        return True





