class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hand = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            hand[bill] += 1
            change = bill - 5
            if change == 5:
                hand[5] -= 1
                if hand[5] < 0:
                    return False
            elif change == 15:
                if hand[10] >= 1 and hand[5] >= 1:
                    hand[10] -= 1
                    hand[5] -= 1
                elif hand[5] >= 3:
                    hand[5] -= 3
                else:
                    return False
        return True